import tqdm 
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
        self.lights = [False] * len(self.target)

    def ready(self):
        return all(l == t for l, t in zip(self.lights, self.target))
        
    def get_pressed(self, i):
        n = Machine()
        n.target = self.target
        n.lights = self.lights.copy()
        n.buttons = self.buttons
        n.pressed = self.pressed.copy()

        n.pressed[i] += 1
        for l in n.buttons[i]:
            n.lights[l] = not n.lights[l]
        return n
    
machines = []         
with open("day10_input.txt", "r") as f:
    for line in f:
        fields = line.split()
        target = fields[0]
        buttons = fields[1:-1] 
        m = Machine()
        m.n = len(target) - 2
        m.target = [c == "#" for c in target[1:-1]]
        for button in buttons:
            numbers = button[1:-1].split(",")
            m.buttons.append(tuple(map(int, numbers)))
        machines.append(m)

result = 0
for machine in tqdm.tqdm(machines):
    already_visited = set()
    machine.start()
    states = [machine]
    while True:
        m = states.pop(0)
        if m.ready():
            result += sum(m.pressed.values())
            break
        lights = "".join(["#" if x else "." for x in m.lights])
        if lights in already_visited:
            continue
        else:
            already_visited.add(lights)
            
        for i in range(len(m.buttons)):
            n = m.get_pressed(i)
            states.append(n)
        
print(result)
