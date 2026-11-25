#!/usr/bin/env python3
"""Midnight Fridge Roast — one-line roast of a smart fridge that refuses
to open after midnight. Writes the entry text to entry.txt."""

import os
import stat

ENTRY = (
    "My fridge locked at 00:07 and asked me to approve the unlock from "
    "the phone I had locked inside it at 23:58, so my midnight snack is "
    "still pending approval."
)


def main():
    # Gate: UTF-8 text, 1-200 characters, one line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert "\n" not in ENTRY and ENTRY.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
