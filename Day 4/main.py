with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

total = 0

for line in lines:
    line = line.split(':')[1]
    line = line.split()
    i = 0
    winning = []
    my = []
    while line[i] != '|':
        winning.append(int(line[i]))
        i += 1
    i += 1
    while i < len(line):
        my.append(int(line[i]))
        i += 1
    count = 0
    for i in my:
        if i in winning:
            count += 1
    if count == 1:
        score = 1
    elif count > 1:
        score = 2**(count-1)
    else:
        score = 0
    
    total += score

print(total)