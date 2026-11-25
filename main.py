#!/usr/bin/env python3
"""Worst Fix Ever — the funniest commit message for a fix that backfired."""
import os

LINE = "fix: stop the crash by deleting the error log; zero crashes reported since"


def main():
    text = LINE.strip()
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 100, "entry must be 1-100 characters"
    assert all(ord(c) >= 32 or c in "\t" for c in text), "no control characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
