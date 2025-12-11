devices = {}
with open("day11_input.txt", "r") as f:
    for line in f:
        source, outputs = line.strip().split(":")
        outputs = outputs.strip().split()
        devices[source] = outputs

def find_paths(from_, end, end2):

    accesible = set(end)
    last_sources = set(end)
    sources = set()

    while last_sources:
        for s in last_sources:
            if s == from_:
                continue
            for source, outputs in devices.items():
                if s in outputs:
                    sources.add(source)
        accesible.update(sources)
        last_sources = sources
        sources = set()
    print("Accesible created.")
        
    paths = [[from_]]
    result = {
        x: 0
        for x in end 
    }
    while paths:

        p = paths.pop(-1)

        
        e = p[-1]

        if e in end2:
            continue
        
        if e in end:
            result[e] += 1
            print("..", result)
            continue
            
        for output in devices[e]:
            if output not in p and output in accesible:
                pp = p.copy()
                pp.append(output)
                paths.append(pp)
                
    return result




res = find_paths("svr", ["fft"], ["out", "dac"])
print(res)
input()
#dac2fft = find_paths("dac", ["fft"], ["out"]) == 0
#print(dac2fft)

fft2dac = find_paths("fft", ["dac"], ["out", "svr"])
print(fft2dac)
input()

dac2out = find_paths("dac", ["out"], ["fft"])
print(dac2out)
input()

#fft2out = find_paths("fft", ["out"], ["dac"])
#print(fft2out)

print(
    #res["dac"] * dac2fft["fft"] * fft2out["out"]
    #+
    res["fft"] * fft2dac["dac"] * dac2out["out"]
)


