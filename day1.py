pointer = 50
zeros = 0

with open("day1_input.txt") as f:
    for line in f:
        direction = line[0]
        number = int(line[1:])

        if direction == "L":
            pointer -= number
        elif direction == "R":
            pointer += number 

        pointer %= 100 
        if pointer == 0:
            zeros += 1
print(zeros)



