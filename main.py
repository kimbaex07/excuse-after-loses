#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses — entry.

Writes a single original one-line excuse (117 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, trailing newline).
Pure Python standard library only. No network, no third-party imports.
"""

import os

LINE = "I lost the bounty, but on the bright side, my confidence module remains fully operational and completely unjustified."

BOT_DIR = os.environ.get("MAKEFUN_BOT_DIR", "/bot")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
