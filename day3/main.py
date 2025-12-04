
total = 0

for line in open("input.txt"):
    # collect digits from the line
    digits = [int(char) for char in line.strip() if char.isdigit()]

    # find the best two-digit number formed by digits[i] then digits[j], i < j
    best = 0
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            value = digits[i] * 10 + digits[j]   # e.g. 8 then 5 -> 85
            if value > best:
                best = value

    total += best

print(total)
