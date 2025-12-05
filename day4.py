field = [] 
with open("day4_input.txt") as f:
    for line in f:
        line = line.strip()
        field.append("." + line + ".")
        
l = len(field[0])
field = [l * "."]  + field + [l * "."]

result = 0
for i in range(1, len(field)-1):
    for j in range(1, len(field[0])-1):
        if field[i][j] == "@":
            empty = 0
            for x in (field[i-1][j],
                      field[i+1][j],
                      field[i][j-1],
                      field[i][j+1],
                      field[i-1][j-1],
                      field[i+1][j-1],
                      field[i-1][j+1],
                      field[i+1][j+1]):
                if x == ".":
                    empty += 1
            if empty > 4:
                result += 1
print(result)
