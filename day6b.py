inputs = [] 
with open("day6_input.txt") as f:
    for line in f:
        line = line.strip("\n")
        inputs.append(line)
        
operators = inputs.pop(-1).split()

l = len(inputs[0])
seps = [-1]
for i in range(l):
    if all(line[i] == " " for line in inputs):
        seps.append(i)
seps.append(l)

new_inputs = []
for line in inputs:
    new_inputs.append([])
    for l, h in zip(seps[:-1], seps[1:]):
        new_inputs[-1].append(line[l+1:h])

inputs = new_inputs

def calc(values, op):
    res = values[0]
    for val in values[1:]:
        if op == "+":
            res += val
        elif op == "*":
            res *= val
        else:
            raise ValueError()
    return res

result = 0 
for i in range(len(operators)):
    op = operators[i]
    values = []
    for j in range(len(inputs[0][i])):
        val = ""
        for line in inputs:
            if line[i][j] != " ":
                val += line[i][j]
        values.append(int(val))
    result += calc(values, op)
print(result)
