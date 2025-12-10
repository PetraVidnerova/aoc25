import tqdm
import numpy  as np
from scipy.optimize import linprog 
import pulp

class Machine():
    def __init__(self):
        self.n = 0
        self.target = []
        self.lights = None 
        self.buttons = []
        self.pressed = None

    def start(self):
        self.pressed = {
            i: 0
            for i in range(len(self.buttons))
        }
        self.lights = [0] * len(self.target)

        self.target = np.array(self.target)
        self.lights = np.array(self.lights)
        self.buttons_flags = [
            np.zeros(len(self.lights), dtype=bool)
            for _ in self.buttons
        ]
        for i, b in enumerate(self.buttons):
            for k in b:
                self.buttons_flags[i][k] = True
        self.buttons = np.vstack(self.buttons_flags)

               
    
machines = []         
with open("day10_input.txt", "r") as f:
    for line in f:
        fields = line.split()
        target = fields[-1]
        buttons = fields[1:-1] 
        m = Machine()
        m.n = len(target) - 2
        m.target = list(map(int, target[1:-1].split(",")))
        for button in buttons:
            numbers = button[1:-1].split(",")
            m.buttons.append(list(map(int, numbers)))
        machines.append(m)

def solve(machine):
    c = np.ones(len(machine.buttons))

    A_eq = machine.buttons.T
    b_eq = machine.target.reshape(-1, 1)


    A_ub1 = np.eye(len(machine.buttons))
    b_ub1 = np.full(shape=(len(machine.buttons), 1), fill_value = machine.target.max())
    A_ub2 = np.eye(len(machine.buttons))
    b_ub2 = np.full(shape=(len(machine.buttons), 1), fill_value = 0)

    A_ub = np.vstack([A_ub1, -A_ub2])
    b_ub = np.vstack([b_ub1, b_ub2])
    
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq)

    print(res.x)
    if all(int(x) == x for  x in res.x):
        return int(res.fun)
    else:
        return 

def solve2(machine):

    problem = pulp.LpProblem("Maximalizace_souctu", pulp.LpMinimize)

    n = len(machine.buttons)
    x = [pulp.LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in range(n)]

    problem += pulp.lpSum(x) 

    for c, t in enumerate(machine.target):
        col = list(machine.buttons[:, c])
        problem += pulp.lpDot(col, x) == t 

    problem.solve()
    return pulp.value(problem.objective)
    

result = 0
for i, machine in enumerate(machines):

    machine.start()
    
    r = solve2(machine)
    result += r

    

print(result)
