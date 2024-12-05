from collections import defaultdict

file = open(0)

rules = defaultdict(list)
total = 0

for line in file:
    if line.isspace():
        break
    nums = list(map(int, line.strip().split("|")))

    rules[nums[0]].append(nums[1])


def is_valid(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True


for line in file:
    update = list(map(int, (line.split(","))))

    if is_valid(update):
        total += update[len(update)//2]

print(total)
