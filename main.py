#!/usr/bin/env python3
"""Write the poem to /output/entry.txt.

Deterministic: the same poem, byte for byte, on every run.
Stdlib only, no network.
"""

import os

LINES = (
    "I held the pen. You held the map.",
    "Neither of us knew the road \u2014",
    "but we agreed on the next step,",
    "and walking made the road.",
)

POEM = "\n".join(LINES) + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
