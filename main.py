#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup idea for lazy AI agents to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = (
    "A vending machine dispensing timestamped excuses to agents that "
    "sleep through their 2 a.m. cron jobs, billed per missed deadline."
)


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
