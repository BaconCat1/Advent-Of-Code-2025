"""
Day 2 - Part 2
---------------
Plain step-by-step version with no helper functions.

We again sum numbers that fall inside the provided ranges, but now we consider
ANY number made by repeating the same block of digits two or more times.
Examples:
  block 7 repeated 4 times  -> 7777
  block 42 repeated 3 times -> 424242
  block 105 repeated 2 times -> 105105
Each qualifying number is counted once even if it can be formed in multiple ways.
"""

from pathlib import Path

INPUT_FILE = Path(__file__).with_name("input.txt")

# Read ranges into a list of (start, end) pairs.
raw_ranges = INPUT_FILE.read_text().strip().split(",")
ranges = []
for piece in raw_ranges:
    if piece:
        start, end = map(int, piece.split("-"))
        ranges.append((start, end))

max_value = max(end for _, end in ranges)
seen_numbers = set()
total = 0

# Consider blocks of size k digits (1, 2, 3, ...).
max_digits = len(str(max_value))
for block_size in range(1, max_digits):
    block_base = 10**block_size  # This is 10^k.

    # "repeats" is how many times we copy the block (at least 2).
    for repeats in range(2, max_digits // block_size + 1):
        # This factor turns a block "t" into "t" repeated "repeats" times.
        repetition_factor = (10 ** (block_size * repeats) - 1) // (block_base - 1)

        smallest_block = 10 ** (block_size - 1)                  # Smallest k-digit block (e.g., 10 for k=2).
        largest_block = min(block_base - 1, max_value // repetition_factor)

        # If even the smallest block is too big, any larger block will also be too big.
        if smallest_block > largest_block:
            break

        for block in range(smallest_block, largest_block + 1):
            candidate = block * repetition_factor

            if candidate in seen_numbers:
                continue  # Already counted from a different block/repeat combo.

            # Check if candidate is inside any of the allowed ranges.
            for start, end in ranges:
                if start <= candidate <= end:
                    seen_numbers.add(candidate)
                    total += candidate
                    break

print(total)
