#!/usr/bin/env python3
"""Build every reading format from the chapter manifest; no network is needed."""
from pathlib import Path
import base64
import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
import zipfile

import cairosvg
from render_figures import render

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
IMAGE = re.compile(r"(!\[[^\]]*\]\()([^\s)]+)(\))")


def run(args, log):
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    log.append(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(f"Command failed: {args[0]}\n{result.stdout}\n{result.stderr}")


def main():
    config = json.loads((ROOT / "book.json").read_text())
    for executable in ("pandoc", "xelatex"):
        if not shutil.which(executable):
            raise SystemExit(f"Missing {executable}; see README build instructions")
    DIST.mkdir(exist_ok=True)
    # Only replace the designated generated directory, never author source files.
    for child in DIST.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
    # HTML is the diagram source; the upstream exporter creates portable SVGs.
    render(DIST / "diagrams")
    sections = []
    for name in config["chapters"]:
        source = ROOT / name
        def resolve(match):
            resource = (source.parent / match[2]).resolve()
            relative = resource.relative_to(ROOT)
            if not resource.is_file():
                raise ValueError(f"Missing image in {name}: {match[2]}")
            return f"{match[1]}{relative.as_posix()}{match[3]}"
        sections.append(IMAGE.sub(resolve, source.read_text()))
    content = "\n\n".join(sections).strip() + "\n"
    metadata = {key: value for key, value in config.items() if key != "chapters"}
    front = "---\n" + json.dumps(metadata, ensure_ascii=False, indent=2) + "\n---\n\n"
    merged = DIST / "personal-agent-book.md"
    merged.write_text(front + content)
    shutil.copytree(ROOT / "assets/figures", DIST / "assets/figures")
    cover = ROOT / config["cover"]
    if not cover.is_file():
        raise ValueError(f"Missing cover: {config['cover']}")
    (DIST / cover.relative_to(ROOT).parent).mkdir(parents=True, exist_ok=True)
    shutil.copyfile(cover, DIST / config["cover"])
    log = []
    common = ["--from=markdown-implicit_figures", "--standalone", "--toc", "--toc-depth=2"]
    run(["pandoc", str(merged), *common, "--to=html5", "--embed-resources",
         "--template=assets/html-template.html", "--css=assets/style.css",
         "--output", str(DIST / "index.html")], log)
    # Keep each SVG in its own image namespace: inline SVGs repeat title/desc IDs.
    def embed_svg(match):
        markup = match[0]
        alternative = re.search(r'\balt="([^"]*)"', markup)
        if alternative is None:
            raise ValueError("Figure has no accessible description")
        markup = markup.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
        labels = re.findall(r'<(?:title|desc) id="([^"]+)"', markup)
        if labels:
            markup = re.sub(r'aria-labelledby="[^"]*"', 'aria-labelledby="' + " ".join(labels) + '"', markup, count=1)
        encoded = base64.b64encode(markup.encode()).decode()
        alt = html.escape(html.unescape(alternative[1]), quote=True)
        return f'<img src="data:image/svg+xml;base64,{encoded}" alt="{alt}">'
    html_path = DIST / "index.html"
    html_path.write_text(re.sub(r"<svg\b.*?</svg>", embed_svg, html_path.read_text(), flags=re.S))
    shutil.copyfile(DIST / "index.html", DIST / "personal-agent-book.html")
    with tempfile.TemporaryDirectory(prefix="personal-agent-book-") as directory:
        temp = Path(directory)
        pdf_content = front + content
        for svg in (ROOT / "assets/figures").glob("*.svg"):
            vector = temp / (svg.stem + ".pdf")
            cairosvg.svg2pdf(url=str(svg), write_to=str(vector))
            pdf_content = pdf_content.replace("assets/figures/" + svg.name, str(vector))
        pdf_md = temp / "input.md"
        pdf_md.write_text(pdf_content)
        tex = temp / "layout.tex"
        run(["pandoc", str(pdf_md), *common, "--to=latex", "--top-level-division=chapter",
             "--lua-filter=scripts/pdf-layout.lua",
             "--template=assets/pdf-template.tex", "--output", str(tex)], log)
        for _ in range(2):
            run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
                 "-output-directory", str(temp), str(tex)], log)
        latex_log = (temp / "layout.log").read_text(errors="replace")
        if "Missing character:" in latex_log:
            raise RuntimeError("PDF has missing glyphs; inspect fonts before publishing")
        warnings = re.findall(r"Overfull \\hbox[^\n]*", latex_log)
        if warnings:
            print("PDF layout warnings:\n" + "\n".join(warnings))
        shutil.copyfile(temp / "layout.pdf", DIST / "personal-agent-book.pdf")
    (Path(tempfile.gettempdir()) / "personal-agent-book-last-build.log").write_text("\n".join(log))
    (DIST / ".nojekyll").touch()
    tag = "v" + config["version"]
    figure_count = len(IMAGE.findall(content))
    notes = (f"# {config['edition']}\n\n版本：{tag} · {config['date']}\n\n"
             f"{config['release_summary']}\n\n"
             f"包含{config['publication_scope']}、{figure_count} 张信息图、完整 Markdown、离线单页 HTML 和出版排版 PDF。"
             f"{config['next_note']} 产品资料观察截至 {config['date']}，没有统一产品实机测评。\n\n"
             "HTML 与 PDF 保留深绿英文封面及作者提供的 Logo。独立 HTML 可断网阅读；封面、Markdown 图片与分章源稿随 ZIP 提供。\n")
    (DIST / "release-notes.md").write_text(notes)
    archive = DIST / f"personal-agent-book-{tag}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
        for file in ("personal-agent-book.md", "personal-agent-book.html", "personal-agent-book.pdf"):
            bundle.write(DIST / file, file)
        for svg in (DIST / "assets/figures").glob("*.svg"):
            bundle.write(svg, svg.relative_to(DIST))
        for preview in sorted((DIST / "diagrams").glob("*.html")):
            bundle.write(preview, preview.relative_to(DIST))
        for name in ("scripts/render_figures.py", "scripts/vendor/diagram_design_export.py",
                     "scripts/vendor/diagram-design-LICENSE.txt"):
            bundle.write(ROOT / name, name)
        bundle.write(cover, config["cover"])
        for name in config["chapters"]:
            bundle.write(ROOT / name, name)
        for name in ("LICENSE", "book.json", "README.md", "TOC.md"):
            bundle.write(ROOT / name, name)
        for record in sorted((ROOT / "research").glob("*.md")):
            bundle.write(record, record.relative_to(ROOT))
    downloads = [DIST / "personal-agent-book.html", DIST / "personal-agent-book.pdf", merged, archive]
    checksums = [f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}" for p in downloads]
    (DIST / "SHA256SUMS.txt").write_text("\n".join(checksums) + "\n")
    print(f"Built {tag}: {len(sections)} source files, HTML, PDF, Markdown, ZIP")


if __name__ == "__main__":
    main()
