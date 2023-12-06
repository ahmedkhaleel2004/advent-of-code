# hyper neutrino solution... so simple its genius

seeds, *blocks = open(0).read().split("\n\n")

seeds = list(map(int,seeds.split(':')[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = [] # update map
    for x in seeds:
        for a, b, c in ranges:
            if b <= x < b + c: # if seed in range
                new.append(x - b + a) # difference plus the start
                break
        else: # for-else: if it was not in the range, it simply maps to itself
            new.append(x)
    seeds = new # update for next block

print(min(seeds))