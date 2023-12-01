with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

sum = 0

for line in lines:
    digits_only = ''.join([char for char in line if char.isdigit()])
    num = ""
    if digits_only:
        num += digits_only[0]
        num += digits_only[-1]
        sum += int(num)

print(sum)