grid = open(0).read().splitlines()

count = 0

for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if grid[r][c] != "A":
            continue
        # now we have an "A", grab the corners and see if they are any of the
        # 4 following patterns that would indicate we have an "X-MAS"
        corners = [grid[r - 1][c - 1], grid[r - 1][c + 1],
                   grid[r + 1][c + 1], grid[r + 1][c - 1]]
        if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
            count += 1

print(count)
