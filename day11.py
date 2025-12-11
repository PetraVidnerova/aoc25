devices = {}
with open("day11_input.txt", "r") as f:
    for line in f:
        source, outputs = line.strip().split(":")
        outputs = outputs.strip().split()
        devices[source] = outputs


paths = [["svr"]]

result = 0 
while paths:

    p = paths.pop(0)

    e = p[-1]
    if e == "dac":
        result += 1
        continue
    
    for output in devices[e]:
        if output not in p:
            pp = p.copy()
            pp.append(output)
            paths.append(pp)
print(result)
            
