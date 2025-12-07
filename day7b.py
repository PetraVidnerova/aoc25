field = [] 
with open("day7_input.txt") as f:
    for line in f:
        field.append(line.strip())
            
index = field[0].index("S")


beams = {index: 1}

for line in field[1:]:
    print(beams)
    new_beams = {} 
    for i, num in beams.items():
        if line[i] == ".":
            new_beams[i] = new_beams.get(i, 0) + num
        elif line[i] == "^":
            new_beams[i-1] = new_beams.get(i-1, 0) + num      
            new_beams[i+1] = new_beams.get(i+1, 0) + num
    beams = new_beams
    
print(sum(beams.values()))
