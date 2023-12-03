import re # regex

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

sumID = 0

for line in lines:
    line = line.split(':')
    this_game = line.pop(0)
    line = line[0]
    line = line.split(';')
    for i in range(len(line)):
        line[i] = line[i].split(',')
    for draw in line:
        for colour in draw:
            count = int(re.findall('\d+', colour)[0]) # regex
            nextLine = False
            if 'red' in colour and count > 12: nextLine = True; break
            if 'blue' in colour and count > 14: nextLine = True; break
            if 'green' in colour and count > 13: nextLine = True; break
        if nextLine: break
    if nextLine: continue
    sumID += int(re.findall('\d+', this_game)[0])

print(f"Part 1: {sumID}")