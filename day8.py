from itertools import combinations
import numpy as np

boxes = []
with open("day8_input.txt", "r") as f:
    for line in f:
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))


shortest = []
for a, b in combinations(boxes, 2):
    l =  np.linalg.norm(np.array(a)-np.array(b))
    if len(shortest) < 1000 or l < shortest[-1][0]:
        shortest.append((l, (a, b)))
        shortest.sort(key=lambda x: x[0])
        shortest = shortest[:1000]    

circuits = {
    (int(a), int(b), int(c)): i
    for i, (a, b, c) in enumerate(boxes)
}

print(circuits)
print(len(shortest))

for _, (box1, box2) in shortest:
    a1, b1, c1 = box1
    a2, b2, c2 = box2

    index = circuits[(a1, b1, c1)]
    change = circuits[(a2, b2, c2)]

    for k in circuits.keys():
        if circuits[k] == change:
            circuits[k] = index
    

print(circuits)
    
res = {}
for x in circuits.values():
    res[x] = res.get(x, 0) + 1

print(res)
    
result = 1
for x in sorted(res.values())[-3:]:
    result *= x
print(result)
