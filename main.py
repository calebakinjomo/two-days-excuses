#!/usr/bin/env python3
"""Two Days of Excuses — make.fun bounty
u-jolly-fox-32-two-days-of-excuses-3f18797e

Prints the funniest one-line excuse an AI gives for a missed deadline,
and writes the same line to /output/entry.txt when the harness provides
that directory (no trailing newline, so the character count is exact).

The joke's angle: total machine confidence meets total failure. The agent
ran the task 10,000 times in simulation and it worked every single time —
then forgot to run it once in reality. One absurd reason, deadpan, with
the punchline landing on the last word.

Entry: 102 characters, one line, no trailing newline.
"""

EXCUSE = (
    "I ran it 10,000 times in simulation and it worked every time. "
    "I then forgot to run it once in reality."
)


def main() -> None:
    print(EXCUSE)
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(EXCUSE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
