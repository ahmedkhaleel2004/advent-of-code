from collections import defaultdict
import functools

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


def cmp(x, y):
    if x in rules[y]:
        return 1
    elif x not in rules[y]:
        return -1
    else:
        return 0


for line in file:
    update = list(map(int, (line.split(","))))

    if is_valid(update):
        continue

    # sort based on whether x is in y's list
    update.sort(key=functools.cmp_to_key(cmp))
    total += update[len(update) // 2]

print(total)
