#!/usr/bin/env python3
"""A Day of One-Line Pitches entry — Variant C: someone like you already did it.

Writes one original persuasive sentence to /output/entry.txt: an ordinary
neighbor with zero coding describes her idea one afternoon and has a working
app by dinner, so the friend's idea could be next. The proof is the neighbor
herself — no coding, one afternoon, a phone passed around at dinner — and the
ask is deliberately tiny: one sentence to start.
Deterministic: same bytes every run. Stdlib only, no network.
"""

import os

LINE = "My neighbor has never written a line of code, but one afternoon she told an AI agent her idea, and by dinner she was passing her phone around showing us the app it built — your idea could be next, and all it takes is one sentence to start."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
