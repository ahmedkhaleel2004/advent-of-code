with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

sum = 0

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in lines:
    # going right for the first number
    digits_only = ""
    temp = ""
    break_flag = False
    for char in line:
        temp += char
        if char.isdigit():
            digits_only += char
            break
        else:
            check = ""
            for i in temp[::-1]:
                check += i
                if check[::-1] in nums:
                    digits_only += str(nums[check[::-1]])
                    break_flag = True
                    break
        if break_flag:
            break
    temp = ""
    break_flag = False
    for char in line[::-1]:
        temp += char
        if char.isdigit():
            digits_only += char
            break
        else:
            check = ""
            for i in temp[::-1]:
                check += i
                if check in nums:
                    digits_only += str(nums[check])
                    break_flag = True
                    break
        if break_flag:
            break
    
    num = ""
    if digits_only:
        num += digits_only[0]
        num += digits_only[-1]
        sum += int(num)

print(sum)