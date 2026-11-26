"""Deadpan forecast for a city that does not exist.

Writes one line, at most 160 characters, to entry.txt in the output
directory (``/output`` on the grader, or ``MAKEFUN_OUTPUT_DIR`` when set
for a local run). The line is a plain, confident broadcast forecast for
Bumbershoot: rain that only falls on people who forgot their umbrella.
"""

import os

FORECAST = (
    "Tonight in Bumbershoot, rain falls only on people who forgot "
    "their umbrella, at a steady 2 inches per hour until 9pm."
)


def main() -> None:
    # Gate: one line, 1 to 160 characters, nothing but the forecast.
    if not 1 <= len(FORECAST) <= 160 or "\n" in FORECAST:
        raise ValueError("forecast must be one line of 1 to 160 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORECAST)
    # No trailing newline: the file holds exactly the forecast line.


if __name__ == "__main__":
    main()
