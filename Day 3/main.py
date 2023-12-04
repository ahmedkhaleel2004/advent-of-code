with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

# with help from the LEGEND MR. HYPER NEUTRINO
# very simple and easy solution
# https://www.youtube.com/watch?v=ZFGX5D9mi-4&ab_channel=HyperNeutrino

cs = set()

for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if dr < 0 or dr >= len(lines) or dc < 0 or dc >= len(lines[dr]) or not lines[dr][dc].isdigit():
                    continue
                while dc > 0 and lines[dr][dc - 1].isdigit():
                    dc -= 1
                cs.add((dr, dc))

ns = []

for r, c in cs:
    s = ""
    while c < len(lines[r]) and lines[r][c].isdigit():
        s += lines[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))