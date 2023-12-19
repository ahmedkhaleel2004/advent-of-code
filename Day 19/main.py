block1, block2 = open(0).read().split("\n\n")

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

ops = { # this is used to map our `cmp` to its proper method
    ">": int.__gt__,
    "<": int.__lt__
}

def accept(item, name = "in"):
    # base cases
    if name == "R":
        return False
    if name == "A":
        return True

    rules, fallback = workflows[name]
    
    for key, cmp, n, target in rules:
        if ops[cmp](item[key], n): # safer than eval(f"{item[key]} {cmp} {n}")
            return accept(item, target) # send it to its next target
    
    return accept(item, fallback) # must be fallback by now

total = 0

for line in block2.splitlines():
    item = {}
    for segment in line[1:-1].split(","):
        ch, n = segment.split("=")
        item[ch] = int(n)
    if accept(item):
        total += sum(item.values())

print(total)