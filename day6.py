inputs = [] 
with open("day6_input.txt") as f:
    for line in f:
        inp = line.strip().split()
        inputs.append(inp)

operators = inputs.pop(-1)

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
    for line in inputs:
        values.append(int(line[i]))
    result += calc(values, op)
print(result)
