left, right, diffs = [], [], []

for line in open(0).read().splitlines():
    nums = line.split(" ")
    left.append(int(nums[0]))
    right.append(int(nums[-1]))

left, right = sorted(left), sorted(right)

for num1, num2 in tuple(zip(left, right)):
    diffs.append(int(max(num1, num2) - min(num1, num2)))

print(sum(diffs))
