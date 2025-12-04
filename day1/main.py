"""
Day 1 - Part 1
---------------
Plain step-by-step version with no helper functions.

We walk around a circular track with 100 positions labeled 0-99.
We start at position 50. Each line in input.txt is an instruction like "L3" or "R12":
  * "L" means move left (toward smaller numbers).
  * "R" means move right (toward larger numbers).
After each move we check whether we landed exactly on position 0.
The program counts how many times that happens.
"""

from pathlib import Path

TRACK_LENGTH = 100
START_POSITION = 50

# Locate the input file that sits next to this script.
INPUT_FILE = Path(__file__).with_name("input.txt")

# Read and clean all lines like "L3" or "R12".
raw_lines = INPUT_FILE.read_text().strip().splitlines()

# Start in the middle of the track.
position = START_POSITION
times_at_zero = 0

# Go through each instruction one by one.
for raw_line in raw_lines:
    direction = raw_line[0]       # Either "L" or "R".
    steps = int(raw_line[1:])     # How far to move.

    # Update our position around the circle.
    if direction == "L":
        position = (position - steps) % TRACK_LENGTH
    else:  # direction == "R"
        position = (position + steps) % TRACK_LENGTH

    # Did we land on position 0?
    if position == 0:
        times_at_zero += 1

# Show the final count.
print(times_at_zero)
