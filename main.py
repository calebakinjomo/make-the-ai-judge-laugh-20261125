#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one office-life joke to /output/entry.txt: a single line
(88 characters) followed by a trailing newline.

The joke is fixed at build time in ENTRY. main() validates that it is
a single non-empty line before writing, so a bad edit fails loudly
instead of producing a malformed entry file. No third-party
dependencies; standard library only.
"""

import os

ENTRY = (
    "I asked my boss for a raise. He said money isn't everything "
    "\u2014 then gave himself a bonus."
)


OUTPUT_DIR = os.environ.get("ENTRY_OUTPUT_DIR", "/output")


def main() -> None:
    if (
        not ENTRY
        or ENTRY != ENTRY.strip()
        or "\n" in ENTRY
        or "\r" in ENTRY
        or len(ENTRY) > 280
    ):
        raise ValueError("ENTRY must be a single non-empty line of at most 280 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
