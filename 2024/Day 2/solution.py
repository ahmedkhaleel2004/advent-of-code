lines = open(0).read().splitlines()
ans = 0

# wow this is like O(n^3) for part 2

for row in lines:
    nums = list(map(int, row.split()))

    def process_nums(nums):
        safe = True
        global ans

        increasing = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
        decreasing = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))

        if not (increasing or decreasing):
            return False

        for i in range(len(nums) - 1):
            print(
                f"{nums} now trying {nums[i]} - {nums[i+1]} which is a diff of {abs(nums[i] - nums[i+1])}")
            if not 1 <= abs(nums[i] - nums[i+1]) <= 3:
                safe = False
                break

        if safe:
            ans += 1

        return safe

    safe = process_nums(nums)

    if not safe:
        for i in range(len(nums)):
            new = nums[:i] + nums[i+1:]
            print(f"{nums} is unsafe, now passing {new}")
            safe = process_nums(new)
            if safe:
                break

print(ans)
