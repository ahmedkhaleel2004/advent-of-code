# lines = []
# with open("/Users/ahmedkhaleel/Repos/advent-of-code/2024/Day 3/test.txt", "r") as file:
#     for line in file:
#         lines.append(line)
# for debugging ^


# THIS CODE BELOW IS MINE AND WORKS!!!

# lines = open(0).read().splitlines()
# ans = 0


# def check_and_add_mult(line: str, i: int) -> int:  # returns how many indices to skip
#     global ans
#     initial_i = i
#     last_char = "m"
#     nums = [0, 0]

#     while (line[i] in "mul(,)" or line[i].isdigit()) and i < len(line):
#         # match-case added in 3.10... im on 3.9
#         i += 1
#         try:
#             if last_char == "m":
#                 assert line[i] == "u"
#                 last_char = "u"
#             elif last_char == "u":
#                 assert line[i] == "l"
#                 last_char = "l"
#             elif last_char == "l":
#                 assert line[i] == "("
#                 last_char = "("
#             elif last_char == "(":
#                 assert line[i].isdigit()
#                 num = 0
#                 # Loop to extract the full number
#                 while i < len(line) and line[i].isdigit():
#                     # Multiply by 10 and add the digit
#                     num = num * 10 + int(line[i])
#                     i += 1  # Move to the next character
#                 assert line[i] == ","
#                 last_char = ","
#                 nums[0] = num
#             elif last_char == ",":
#                 assert line[i].isdigit()
#                 num = 0
#                 # Loop to extract the full number
#                 while i < len(line) and line[i].isdigit():
#                     # Multiply by 10 and add the digit
#                     num = num * 10 + int(line[i])
#                     i += 1  # Move to the next character
#                 assert line[i] == ")"
#                 last_char = ")"
#                 nums[1] = num
#             elif last_char == ")":
#                 ans += nums[0] * nums[1]
#                 break
#         except AssertionError:
#             return 1  # move normally

#     return i - initial_i


# for line in lines:
#     i = 0
#     while i < len(line):
#         if line[i] == "m":
#             i += check_and_add_mult(line, i)
#         else:
#             i += 1

# print(ans)

# for part 1 at least... its pretty easy to modify for part 2 but come one lets just use regex like normal humans

import re

# no splitlines here simply returns one whole string with \n in them
memory = open(0).read()

on = True
total = 0

for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory):
    if match == "do()":
        on = True
    elif match == "don't()":
        on = False
    elif on:
        x, y = map(int, match[4:-1].split(","))
        total += x * y

print(total)
