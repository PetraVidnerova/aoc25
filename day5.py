ranges = []
ids = [] 
with open("day5_input.txt", "r") as f:
    is_ranges = True
    for line in f:
        line = line.strip()
        if is_ranges:
            if not line:
                is_ranges = False
            else:
                l, u = line.split("-")
                ranges.append((int(l), int(u)))
        else:
            ids.append(int(line))

result = 0
for x in ids:
    for l, u in ranges:
        if l <= x <= u:
            result += 1
            break
print(result)
