lines = open(0).read().splitlines()
ans = 0

for row in lines:
    safe = True
    nums = list(map(int, row.split()))

    increasing = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
    decreasing = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))

    if not (increasing or decreasing):
        continue

    for i in range(len(nums) - 1):
        if not 1 <= abs(nums[i] - nums[i+1]) <= 3:
            safe = False
            break

    if safe:
        ans += 1

print(ans)
