#!/usr/bin/env python3
"""Check the deployed public files against the exact build artifacts."""
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen
import hashlib
import sys
import time

DIST = Path(__file__).resolve().parents[1] / "dist"


def main():
    base = sys.argv[1].rstrip("/") + "/"
    expected = {"index.html": hashlib.sha256((DIST / "index.html").read_bytes()).hexdigest()}
    for line in (DIST / "SHA256SUMS.txt").read_text().splitlines():
        digest, filename = line.split("  ", 1)
        expected[filename] = digest
    for attempt in range(12):
        try:
            verified = []
            for filename, digest in expected.items():
                url = base if filename == "index.html" else urljoin(base, filename)
                request = Request(url, headers={"User-Agent": "personal-agent-book-publication-check"})
                with urlopen(request, timeout=20) as response:
                    assert response.status == 200, f"HTTP {response.status}: {filename}"
                    content = response.read()
                assert hashlib.sha256(content).hexdigest() == digest, f"Published content differs: {filename}"
                verified.append(f"HTTP 200, SHA256 matches: {filename} ({len(content)} bytes)")
            print("\n".join(verified))
            print(f"Public reading and downloads verified: {base}")
            return
        except (OSError, AssertionError) as error:
            if attempt == 11:
                raise
            print(f"Waiting for Pages propagation ({attempt + 1}/12): {error}", flush=True)
            time.sleep(5)


if __name__ == "__main__":
    main()
