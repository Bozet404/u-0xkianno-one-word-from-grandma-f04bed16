#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes the single word our grandma would text about AI to /output/entry.txt.

The word is "Robit": the typo a grandma would actually make while trying
to type "robot" on her phone — warm, a little baffled, and unmistakably
about the machine she is trying to describe.
"""

import os

WORD = "Robit"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
