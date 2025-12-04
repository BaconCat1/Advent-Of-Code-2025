def max_joltage_for_bank(bank: str, k: int) -> int:
    digits = bank.strip()
    n = len(digits)
    if k > n:
        raise ValueError("Bank has fewer than k digits")

    to_remove = n - k
    stack = []

    for ch in digits:
        while to_remove > 0 and stack and stack[-1] < ch:
            stack.pop()
            to_remove -= 1

        stack.append(ch)

    result_digits = stack[:k]
    return int("".join(result_digits))

def main():
    k = 12
    total = 0

    # ALWAYS read input.txt
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += max_joltage_for_bank(line, k)

    print(total)

if __name__ == "__main__":
    main()
