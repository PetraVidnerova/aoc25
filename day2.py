with open("day2_input.txt", "r") as f:
    input_ = f.read().strip()

items = input_.split(",")
items = list(map(lambda x: x.split("-"), items))

invalid = [] 

print(items)
for a, b in items:
    a, b = int(a), int(b)
    for x in range(a, b+1):
        s = str(x)
        if s[:len(s)//2] == s[len(s)//2:]:
            invalid.append(x)

print(invalid)
print(sum(invalid))
            
