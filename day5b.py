import tqdm 
ranges = []
ids = [] 
with open("day5_input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        else:
            l, u = line.split("-")
            ranges.append((int(l), int(u)))

dis_ranges = [] 
ranges = sorted(ranges)

low = [l for l, u in ranges]
up = [u for l, u in ranges]

# merge intervals
start = 0
while start < len(low)-1:
    if low[start+1] <= up[start]+1:
        up[start] = max(up[start], up[start+1])
        del low[start+1]
        del up[start+1]
    else:
        start += 1

sizes = [u-l+1 for u, l in zip(up, low)]
print(sum(sizes))
        


