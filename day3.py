banks = []
with open("day3_input.txt") as f:
    for line in f:
        line = line.strip()
        i, d1 = max(enumerate(line[:-1]), key=lambda x: x[1])
        d2 = max(line[i+1:])
        banks.append(int(d1+d2))
print(sum(banks))