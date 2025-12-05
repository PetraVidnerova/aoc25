banks = []
with open("day3_input.txt") as f:
    for line in f:
        line = line.strip()
        digits = []
        start = 0
        for i in range(12):
            e = 11-i
            if e == 0:
                e = len(line) + 1
            else:
                e = -e 
            s, d = max(enumerate(line[start:e]), key=lambda x: x[1])
            start += s + 1
            digits.append(d)

        banks.append(int("".join(digits)))
print(sum(banks))