#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun bounty entry.

Writes one office-life joke to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked my boss for a raise. He said money isn't everything "
    "\u2014 then gave himself a bonus."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
