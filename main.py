#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter, written to be funny.

The program writes exactly one line to /output/entry.txt: a resignation
letter from an office worker who has spent four years answering every
email with "per my last email", and who finally turns the phrase back
on the job itself. Deterministic: no input, no randomness, no network,
no clock — the same line on every run.
"""

import os
import sys

LINE = (
    "I hereby resign, effective immediately \u2014 after four years of "
    "'per my last email,' I have decided to per my last day."
)

MAX_CHARS = 140


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate self-check: one line, 1-140 chars, not only whitespace, no
    # control characters, no trailing space.
    text = LINE.strip()
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert all(ord(c) >= 0x20 or c in "\t" for c in text), "no control chars"
    assert text == text.rstrip(), "no trailing space"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    assert text.strip(), "entry must not be only whitespace"

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")

    # Read back and verify byte-exactly what was written.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "read-back mismatch"
    assert len(written.rstrip("\n")) == len(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
