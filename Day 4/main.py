with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

m = {} # lets keep track of the count of every card

for idx, line in enumerate(lines): # easy card number

    if idx not in m: # first case and if not from prev card
        m[idx] = 1

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
    
    for n in range(idx + 1, idx + count + 1): # for next up till i + count
        m[n] = m.get(n, 1) + m[idx] # update the value in the map, with default just incase
        # we add m[i] because the number of times we have the current card
        # is the number of times we need to add to the next card check
        # absolutely genius

# part 2 logic from hyper neutrino
# https://www.youtube.com/watch?v=uxShpk__9xE&ab_channel=HyperNeutrino

print(sum(m.values()))