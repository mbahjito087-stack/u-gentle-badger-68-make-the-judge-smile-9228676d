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

DEFAULT_OUTPUT_DIR = "/output"
DEST_NAME = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, DEST_NAME)
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    with open(dest, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == TEXT, "entry.txt differs from the line after writing"
    print(f"wrote {dest} ({len(TEXT)} chars, one line)")


if __name__ == "__main__":
    main()
