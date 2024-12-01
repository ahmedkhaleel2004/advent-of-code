with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# with help from the LEGEND MR. HYPER NEUTRINO
# very simple and easy solution
# https://www.youtube.com/watch?v=ZFGX5D9mi-4&ab_channel=HyperNeutrino

total = 0

for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch != '*':
            continue

        cs = set()

        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if dr < 0 or dr >= len(lines) or dc < 0 or dc >= len(lines[dr]) or not lines[dr][dc].isdigit():
                    continue
                while dc > 0 and lines[dr][dc - 1].isdigit():
                    dc -= 1
                cs.add((dr, dc))

        if len(cs) != 2:
            continue

        ns = []

        for cr, cc in cs:
            s = ""
            while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                s += lines[cr][cc]
                cc += 1
            ns.append(int(s))
        
        total += ns[0] * ns[1]

print(total)