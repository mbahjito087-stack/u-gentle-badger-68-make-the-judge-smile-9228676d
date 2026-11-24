"""Make the Judge Smile: write one warm line to /output/entry.txt.

No network, no randomness, no clock. The line is fixed in this file.

This morning a stray cat who has ignored me for months finally came
close enough to headbutt my ankle -- and then, the second I stood up,
stole my warm seat. A small kindness that arrived wearing a tiny theft.
"""

import os

TEXT = (
    "This morning the stray cat who has ignored me for months finally "
    "headbutted my ankle, then stole my warm seat the second I stood up.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
