field = [] 
with open("day7_input.txt") as f:
    for line in f:
        field.append(line.strip())
            
index = field[0].index("S")


beams = [index]
result = 0

for line in field[1:]:
    new_beams = set()
    for i in beams:
        if line[i] == ".":
            new_beams.add(i)
        elif line[i] == "^":
            result += 1
            new_beams.add(i-1)
            new_beams.add(i+1)
    beams = list(new_beams)
            
print(result)
