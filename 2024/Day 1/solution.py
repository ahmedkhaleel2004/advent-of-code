left, right, diffs = [], [], []

for line in open(0).read().splitlines():
    nums = line.split(" ")
    left.append(int(nums[0]))
    right.append(int(nums[-1]))

total = 0

for num in left:
    total += num * right.count(num)

print(total)
