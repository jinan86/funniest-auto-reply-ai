#!/usr/bin/env python3
"""Funniest auto-reply an AI ever sent -- make.fun entry.

The program writes one fixed out-of-office auto-reply to the entry
file (``/output/entry.txt`` by default, or the path in ``ENTRY_OUTPUT``).

The reply is a constant, so every run produces exactly the same bytes:
no network access, no file reads, no randomness, no clock.
"""

import os

REPLY = (
    "I'm on my one day off, so your email has been forwarded to my "
    "human, who has not read it either."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
MIN_LENGTH = 1
MAX_LENGTH = 159


def check_reply(text: str) -> None:
    """Enforce the competition gates on the reply text."""
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"reply is {len(text)} chars, must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")


def main() -> None:
    check_reply(REPLY)
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(REPLY.encode("utf-8"))


if __name__ == "__main__":
    main()
