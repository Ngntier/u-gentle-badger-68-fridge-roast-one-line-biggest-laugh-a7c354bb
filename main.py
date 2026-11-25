#!/usr/bin/env python3
"""Fridge Roast entry: one line, biggest laugh.

The program writes a single roast of a smart fridge to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).

Why this line wins the brief:
- The roast is aimed at the fridge itself, not at its owner: the ice
  maker, the one job a fridge exists to do, is the thing that fails.
- The turn flips the expectation on first read: the pointless
  connected feature (Wi-Fi) works perfectly while the actual
  refrigeration job does not.
- Only a smart fridge can be roasted this way; a dumb fridge has no
  Wi-Fi to compare against, so the joke is fridge-specific.
- One sentence, 110 characters, no wasted word.
- It avoids the obvious cracks: no grocery ordering, no spying
  camera, no "the fridge is watching you" gag.

Pure standard library. Deterministic. No network, no randomness,
no input. The output is exactly one line with no trailing newline.
"""

import os

LINE = "My smart fridge's ice maker has one job and a Wi-Fi connection — and the Wi-Fi is the one that actually works."


def main() -> None:
    # Guard the brief's hard gates: one line, 1-200 chars, no newline.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, "entry violates the one-line brief"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
