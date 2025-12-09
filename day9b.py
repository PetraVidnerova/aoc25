from itertools import combinations
import tqdm
import random

coords = [] 
minx, maxx = None, None
miny, maxy = None, None

with open("day9_input.txt", "r") as f:
    for line in f:
        x, y = line.split(",")
        x, y = int(x), int(y)
        coords.append((x, y))

minx = min(x for x, y in coords)
maxx = max(x for x, y in coords)

miny = min(y for x, y in coords)
maxy = max(y for x, y in coords)

horizontal = []
vertical = [] 


for x, y in zip(coords, coords[1:] + coords[:1]):
    if x[0] == y[0]:
        horizontal.append(
            (x[0], (min(x[1], y[1]), max(x[1], y[1])))
        )
    elif x[1] == y[1]:
        vertical.append(
            (x[1], (min(x[0], y[0]), max(x[0], y[0])))
        )
    else:
        raise ValueError()

horizontal.sort(key=lambda x: x[0])
vertical.sort(key=lambda x: x[0])
    
def inside(x, y):
    lefside = 0
    upside = 0
    for by, (minx, maxx) in vertical:
        if by == y and minx <= x <= maxx:
            return True
        if by < y and minx <= x < maxx:
            lefside += 1
        if by > y:
            break
    for bx, (miny, maxy) in horizontal:
        if bx == x and miny <= y <= maxy:
            return True
        if bx < x and miny <= y < maxy:
            upside += 1
        if bx > x:
            break
    if lefside % 2 and upside % 2:
        return True
    else:
        return False
"""
for x in range(0, 12):
    for y in range(0, 12):
        if inside(y, x):
            print("X", end="")
        else:
            print(".", end="")
    print()
exit()
"""

def valid(a, b):
    if not inside(a[0], a[1]):
        return False
    if not inside(a[0], b[1]):
        return False
    if not inside(b[0], a[1]):
        return False
    if not inside(b[0], b[1]):
        return False
    
    borders = [(x, a[1]) for x in range(min(a[0], b[0]), max(a[0], b[0])+1)]
    borders += [(x, b[1]) for x in range(min(a[0], b[0]), max(a[0], b[0])+1)]
    borders += [(a[0], x) for x in range(min(a[1], b[1]), max(a[1], b[1])+1)]
    borders += [(b[0], x) for x in range(min(a[1], b[1]), max(a[1], b[1])+1)]

    random.shuffle(borders)
                                         
    for (x, y) in borders:
        if not inside(x, y):
            return False
    return True

squares = []
for a, b in tqdm.tqdm(combinations(coords, 2), total=int(len(coords)*(len(coords)-1)/2)):
    volume = (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)
    squares.append((volume, (a, b)))
    
squares.sort(key=lambda x: x[0], reverse=True)

for volume, (a, b) in tqdm.tqdm(squares):
    if valid(a, b):
        print(volume)
        break
