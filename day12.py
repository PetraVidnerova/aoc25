import numpy as np
from scipy.ndimage import rotate
import tqdm

shapes = []
sizes = []
counts = [] 

with open("day12_input.txt", "r") as f:
    is_shapes = True
    in_shape = 0
    for line in f:
        if "x" in line:
            is_shapes = False
        if is_shapes:
            if in_shape == 0:
                new_shape = []
                in_shape += 1
            elif 1 <= in_shape <= 3:
                new_shape.append(
                    np.array([x == "#" for x in line.strip()], dtype=int)
                )
                in_shape += 1
            elif in_shape == 4:
                shapes.append(np.vstack(new_shape))
                in_shape = 0
        else:
            size, numbers = line.strip().split(":")
            x, y = size.split("x")
            x, y = int(x), int(y)
            if x < y:
                x, y = y, x 
            sizes.append((x, y))
            numbers = numbers.split()
            numbers = list(map(int, numbers))
            counts.append(numbers)


asignments = sorted(zip(sizes, counts), key=lambda x: (-(x[0][0]*x[0][1]), sum(x[1])))
            
import pulp

def fits2(x, y, shapes, counts):
    size = x * y
    C = 0 
    for sh, c in zip(shapes, counts):
        C += c * sh.sum()
    if C > size:
        print("UGH")
        return 0
    
    problem = pulp.LpProblem("Maximalizace_souctu", pulp.LpMinimize)

    all_shapes = []
    for sh in shapes:
        rot_shapes = []
        for angle in 0, 90, 180, 270:
            rot_shapes.append(rotate(sh, angle=angle))
        all_shapes.append(rot_shapes)

    all_variables = []
    bin_variables = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append([])
        bin_variables.append(row)
        

    shapes_counts = []
    for s in shapes:
        row = []
        for _ in range(4):
            row.append([])
        shapes_counts.append(row)
                             
        
    for i in range(x-2):
        for j in range(y-2):
            for ki, l in enumerate(all_shapes):
                for k, s in enumerate(l):
                    X = pulp.LpVariable(f"s_{i}_{j}_{ki}_{k}", cat="Binary")
                    all_variables.append(X)
                    shapes_counts[ki][k].append(X)
                    for ii in range(3):
                        for jj in range(3):
                            if s[ii, jj] == 1:
                                bin_variables[i+ii][j+jj].append(X)
    
    problem += pulp.lpSum(all_variables)

    for i in range(x):
        for j in range(y):
            problem += pulp.lpSum(bin_variables[i][j]) <= 1
            
    for s, c in zip(shapes_counts, counts):
        problem += pulp.lpSum(s) == c
        
    res = problem.solve()
    print(pulp.value(problem.objective))
    if res == 1:
        return 1
    else:
        return 0
            

        
res = 0
not_solved = [] 
for (x, y), c in tqdm.tqdm(asignments):
    
    print(x, y, c)
    for x1, y1, c1 in not_solved:
        if x <= x1 and y <= y1:
            if all([cc1 <= cc for cc1, cc in zip(c1, c)]):
                print("SKIPPING")
                continue
    r =  fits2(x, y, shapes,c)
    if r == 0:
        not_solved.append((x, y, c))
    res += r
print(res)
