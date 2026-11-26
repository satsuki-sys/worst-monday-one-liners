#!/usr/bin/env python3
"""Write one funny line about an AI agent's worst Monday.

The line stacks three concrete Monday miseries (a deploy frozen at 99%,
an inbox at 4,000 unread, a stand-up that should have been a message)
and ends on the agent's escape hatch: marking itself away and blaming
Tuesday-me, the version of itself that does not exist yet.
"""

import os

ENTRY = (
    "My deploy froze at 99%, inbox hit 4,000, stand-up should've been "
    "a message — so I set my status to 'away' and blamed Tuesday me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
