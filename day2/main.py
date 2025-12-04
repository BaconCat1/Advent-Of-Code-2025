"""
Day 2 - Part 1
---------------
Plain step-by-step version with no helper functions.

The input is a list of ranges like "10-90,120-150".
We need to find every number that is just some digits repeated twice in a row
(for example "37" -> "3737", or "482" -> "482482") and add up the ones that
fall inside any of the given ranges.
"""

from pathlib import Path

INPUT_FILE = Path(__file__).with_name("input.txt")

# Read ranges like "10-90,120-150" into a list of (start, end) pairs.
raw_ranges = INPUT_FILE.read_text().strip().split(",")
ranges = []
for piece in raw_ranges:
    if piece:
        start, end = map(int, piece.split("-"))
        ranges.append((start, end))

# The biggest number in all ranges tells us how far we need to search.
max_value = max(end for _, end in ranges)

total = 0

# Look at numbers made of two identical halves: "t" followed by "t".
# If "t" has k digits, the doubled number equals t * (10^k + 1).
max_digits = len(str(max_value))
for block_size in range(1, max_digits // 2 + 1):
    multiplier = 10**block_size + 1
    smallest_block = 10 ** (block_size - 1)             # Smallest k-digit block.
    largest_block = min(10**block_size - 1, max_value // multiplier)  # Largest that keeps us under the max range.

    for block in range(smallest_block, largest_block + 1):
        candidate = block * multiplier

        # Check if candidate falls in any allowed range.
        for start, end in ranges:
            if start <= candidate <= end:
                total += candidate
                break  # Don't add it twice.

print(total)
