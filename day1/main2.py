"""
Day 1 - Part 2
---------------
Plain step-by-step version with no helper functions.

Same circular track as Part 1 (100 positions, start at 50), but now we count
how many times we cross position 0 during each move. A single instruction can
wrap around the track multiple times.
"""

from pathlib import Path

TRACK_LENGTH = 100
START_POSITION = 50
INPUT_FILE = Path(__file__).with_name("input.txt")

# Read all instructions as raw strings.
raw_lines = INPUT_FILE.read_text().strip().splitlines()

position = START_POSITION
crossings = 0

for raw_line in raw_lines:
    direction = raw_line[0]
    steps = int(raw_line[1:])

    # Figure out how many steps until we would reach position 0.
    if direction == "R":
        distance_to_zero = (TRACK_LENGTH - position) % TRACK_LENGTH
    else:  # direction == "L"
        distance_to_zero = position % TRACK_LENGTH

    # If we are already at 0, the next time we "cross" it is one full lap away.
    if distance_to_zero == 0:
        distance_to_zero = TRACK_LENGTH

    # Count how many times we cross position 0 during this instruction.
    if steps >= distance_to_zero:
        extra_steps_after_first_cross = steps - distance_to_zero
        crossings += 1 + extra_steps_after_first_cross // TRACK_LENGTH

    # Update our position after taking the steps.
    if direction == "L":
        position = (position - steps) % TRACK_LENGTH
    else:
        position = (position + steps) % TRACK_LENGTH

print(crossings)
