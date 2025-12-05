import re
with open("day2_input.txt", "r") as f:
    input_ = f.read().strip()

items = input_.split(",")
items = list(map(lambda x: x.split("-"), items))

invalid = [] 
pattern = re.compile(r'(\d+)\1+')

print(items)
for a, b in items:
    a, b = int(a), int(b)
    for x in range(a, b+1):
        s = str(x)
        if pattern.fullmatch(s):
            invalid.append(x)
print(sum(invalid))
            
