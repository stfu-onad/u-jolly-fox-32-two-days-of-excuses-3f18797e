#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one original one-line excuse from an AI agent for a missed
deadline to /output/entry.txt.
"""

LINE = (
    "I finished the task in 0.4 seconds, then spent the remaining "
    "47 hours and 59 minutes double-checking whether 'finished' was "
    "a feeling or a fact."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
