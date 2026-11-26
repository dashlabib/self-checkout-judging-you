#!/usr/bin/env python3
"""The Self-Checkout Is Judging You -- make.fun entry.

Writes one funny remark, in the voice of a judgmental self-checkout
machine, to /output/entry.txt. Pure Python standard library, fully
deterministic: every run writes exactly the same bytes.

The competition gate: /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. This program validates that gate
itself before writing, and writes the line with no trailing newline,
so the file holds exactly the remark.
"""

import os
import sys

# The entry: a single line from a smug self-checkout machine to a
# shopper buying twelve yoghurts and nothing else.
LINE = (
    "Twelve yoghurts, no spoon, no plan. "
    "Your loyalty card just asked to be transferred "
    "to someone with a kitchen."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, gate needs 1..{MAX_CHARS}"
        )
    if not line.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)
    print(
        f"chars={len(LINE)} bytes={len(LINE.encode('utf-8'))} -> {path}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
