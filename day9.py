from itertools import combinations

coords = [] 
with open("day9_input.txt", "r") as f:
    for line in f:
        x, y = line.split(",")
        coords.append((int(x), int(y)))

largest = 0
for a, b in combinations(coords, 2):
    volume = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
    if volume > largest:
        largest = volume

print(largest)
