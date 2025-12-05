pointer = 50
zeros = 0

with open("day1_input.txt") as f:
    for line in f:
        direction = line[0]
        number = int(line[1:])

        if number > 100:
            zeros += number // 100
            number %= 100 

        if number == 0:
            continue 
        last = pointer 

        if direction == "L":
            pointer -= number
        elif direction == "R":
            pointer +=  number 

        if last > 0 and pointer <= 0:
            zeros +=  1  
        elif pointer >= 100:
            zeros += 1 
        
        pointer %= 100 

print(zeros)



