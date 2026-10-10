#!/usr/bin/env python3
"""Validate the actual publication: offline resources, links, PDF fonts and bundle."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import base64
import hashlib
import json
import re
import subprocess
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


class Publication(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.images, self.external = set(), [], [], []
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate HTML ID: {attrs['id']}"
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs.get("src", ""))
            assert attrs.get("alt"), "Image without text alternative"
        if tag in ("script", "link"):
            resource = attrs.get("src") or attrs.get("href", "")
            if resource and not resource.startswith("data:"):
                self.external.append(resource)


def main():
    config = json.loads((ROOT / "book.json").read_text())
    document = Publication()
    html = (DIST / "index.html").read_text()
    document.feed(html)
    html_text = re.sub(r"\s+", "", "".join(document.text))
    assert not document.external, f"External HTML dependencies: {document.external}"
    assert document.images and all(i.startswith("data:") for i in document.images), "Images aren't embedded"
    for resource in document.images:
        assert resource.startswith("data:image/svg+xml;base64,"), "Unexpected figure format"
        svg = ET.fromstring(base64.b64decode(resource.split(",", 1)[1], validate=True))
        assert svg.tag == "{http://www.w3.org/2000/svg}svg", "Figure has no SVG namespace"
        assert svg.get("viewBox"), "Figure has no scalable viewport"
    for link in document.links:
        parsed = urlsplit(link)
        if link.startswith("#"):
            assert unquote(link[1:]) in document.ids, f"Broken HTML anchor: {link}"
        elif not parsed.scheme and parsed.path:
            assert (DIST / unquote(parsed.path)).is_file(), f"Missing download: {link}"
    expected_images = 0
    for name in config["chapters"]:
        source = ROOT / name
        text = source.read_text()
        heading = text.splitlines()[0].removeprefix("# ")
        assert re.sub(r"\s+", "", heading) in html_text, f"Chapter missing from HTML: {name}"
        assert "cite" not in text and "TODO" not in text, f"Unresolved draft markers: {name}"
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            assert (source.parent / target).is_file(), f"Missing source image: {target}"
            expected_images += 1
    assert len(document.images) == expected_images, "Some chapter figures were omitted"
    assert (DIST / "index.html").read_bytes() == (DIST / "personal-agent-book.html").read_bytes()
    pdf = DIST / "personal-agent-book.pdf"
    fonts = subprocess.check_output(["pdffonts", str(pdf)], text=True)
    font_rows = fonts.splitlines()[2:]
    assert font_rows and all(re.search(r"\s+yes\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", row) for row in font_rows), "Unembedded PDF fonts"
    pdf_text = subprocess.check_output(["pdftotext", str(pdf), "-"], text=True)
    compact = re.sub(r"\s+", "", pdf_text)
    for name in config["chapters"]:
        title = (ROOT / name).read_text().splitlines()[0].removeprefix("# ")
        assert re.sub(r"\s+", "", title) in compact, f"Chapter missing from PDF: {name}"
    for line in (DIST / "SHA256SUMS.txt").read_text().splitlines():
        digest, filename = line.split("  ", 1)
        assert hashlib.sha256((DIST / filename).read_bytes()).hexdigest() == digest, f"Checksum mismatch: {filename}"
    archive = DIST / f"personal-agent-book-v{config['version']}.zip"
    with zipfile.ZipFile(archive) as bundle:
        assert bundle.testzip() is None, "Corrupt ZIP"
        for name in config["chapters"]:
            assert name in bundle.namelist(), f"Chapter source missing from ZIP: {name}"
        markdown = bundle.read("personal-agent-book.md").decode()
        for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", markdown):
            assert target in bundle.namelist(), f"Markdown image missing from ZIP: {target}"
    print(f"Publication verified: {len(config['chapters'])} sources, {len(document.images)} embedded figures, links, PDF fonts/text, ZIP, checksums")


if __name__ == "__main__":
    main()
