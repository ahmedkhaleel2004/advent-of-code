points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

b = 0

# this is the math solution
# count boundary points and use shoelace theorem to find initial area (meaningless)
# then subtract boundary points and add them to inside points

for line in open(0):
    _, _, x = line.split()
    x = x[2:-1]
    dr, dc = dirs["RDLU"[int(x[-1])]] # use it as index
    n = int(x[:-1], 16) # convert to base 10
    b += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1

# math solution is always the faster solution
# this runs in same time

print(i + b)