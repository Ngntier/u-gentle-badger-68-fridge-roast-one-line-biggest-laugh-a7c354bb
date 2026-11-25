#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes one roast of a smart fridge to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output). Pure standard library; deterministic; no network,
no input.
"""

import os

ROAST = "My smart fridge's ice maker has one job and a Wi-Fi connection \u2014 and the Wi-Fi is the one that actually works."

# Candidates weighed against the judge brief, in its order
# (1. roast aimed at the fridge itself, 2. punchline lands on first read,
#  3. specific to smart fridges, 4. tight wording, 5. fresh angle):
# 1. "My smart fridge updated its firmware at 3 a.m. and now needs a minute
#    to think before admitting there's no milk."
#    Firmware + milk is on-subject and specific, but "needs a minute to
#    think" is a soft punchline: the turn is a shrug, not a laugh.
# 2. "The fridge's app texted me that the milk expired. It knew for three
#    days and waited until I was already pouring."
#    Good turn (it knew and waited), very fridge-specific, but two sentences
#    and the setup eats half the line before the joke arrives.
# 3. "It can stream music, show recipes, and track my diet \u2014 it just can't
#    make ice, which is the one thing a fridge is for."
#    Decent list-then-drop structure, but "track my diet" is a generic
#    smart-gadget gag that would work on any device with an app.
# 4. "My fridge rebooted during a firmware update and forgot what cold is.
#    The milk found out first."
#    Funny and specific, but two sentences and the second one explains the
#    first joke's fallout instead of landing a new turn.
# 5. "My smart fridge's ice maker has one job and a Wi-Fi connection \u2014 and
#    the Wi-Fi is the one that actually works."
#    Picked: the roast is aimed squarely at the fridge (its ice maker, the
#    one job a fridge exists for); the turn flips the expectation \u2014 the
#    pointless connected feature works, the actual fridge part doesn't;
#    it is specific to smart fridges (a dumb fridge has no Wi-Fi to compare
#    against); one sentence, no wasted word; and it dodges the obvious
#    cracks the brief warns against (no grocery ordering, no spying camera).
#    110 chars, 22 words, one line, no trailing newline.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
