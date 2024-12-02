# lines = open(0).read().splitlines()
# ans = 0

# # wow this is like O(n^3) for part 2

# for row in lines:
#     nums = list(map(int, row.split()))

#     def process_nums(nums):
#         safe = True
#         global ans

#         increasing = all(nums[i] < nums[i + 1] for i in range(len(nums) - 1))
#         decreasing = all(nums[i] > nums[i + 1] for i in range(len(nums) - 1))

#         if not (increasing or decreasing):
#             return False

#         for i in range(len(nums) - 1):
#             print(
#                 f"{nums} now trying {nums[i]} - {nums[i+1]} which is a diff of {abs(nums[i] - nums[i+1])}")
#             if not 1 <= abs(nums[i] - nums[i+1]) <= 3:
#                 safe = False
#                 break

#         if safe:
#             ans += 1

#         return safe

#     safe = process_nums(nums)

#     if not safe:
#         for i in range(len(nums)):
#             new = nums[:i] + nums[i+1:]
#             print(f"{nums} is unsafe, now passing {new}")
#             safe = process_nums(new)
#             if safe:
#                 break

# print(ans)

# mz soln, better format, same logic

lines = open(0).read().splitlines()
reports = [list(map(int, line.split())) for line in lines]


def is_safe(report):
    difference = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    if all(1 <= diff <= 3 for diff in difference):
        return True
    elif all(-3 <= diff <= -1 for diff in difference):
        return True
    return False


def can_be_made_safe(rSeport):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False


safe_count = 0
for report in reports:
    if is_safe(report) or can_be_made_safe(report):
        safe_count += 1
print(safe_count)
