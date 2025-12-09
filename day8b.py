import tqdm 
from itertools import combinations
import numpy as np

boxes = []
with open("day8_input.txt", "r") as f:
    for line in f:
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))


shortest = []
for a, b in tqdm.tqdm(combinations(boxes, 2)):
    l =  np.linalg.norm(np.array(a)-np.array(b))
    shortest.append((l, (a, b)))

shortest.sort(key=lambda x: x[0])

circuits = {
    b: i
    for i, b in enumerate(boxes)
}

circuits2 = {i: [b] for i, b in enumerate(boxes)}

for _, (box1, box2) in shortest:

    index = circuits[box1]
    change = circuits[box2]

    if index == change:
        continue
    
    for b in circuits2[change]:
        circuits[b] = index

    circuits2[index] += circuits2[change]
    del circuits2[change]

    if len(circuits2) == 1:
        print(box1[0] * box2[0])
        break
    
