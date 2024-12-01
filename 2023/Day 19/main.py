block1, _ = open(0).read().split("\n\n")

workflows = {}

# just a bunch of input processing maps the rules and fallback of a workflow

for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, cmp, n, target))

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        # updating the ranges
        if cmp == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)

        # check for empty ranges
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target) # i cannot properly explain what is happening here
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F # but this updates the ranges again using the false range
        else:
            break
    else:
        total += count(ranges, fallback) # if didnt break, not included in rules -> fallback
            
    return total

print(count({key: (1, 4000) for key in "xmas"}))