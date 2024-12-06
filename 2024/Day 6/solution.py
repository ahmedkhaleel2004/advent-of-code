# very unoptimized and ugly

grid = [list(row) for row in open(0).read().splitlines()]

seen = set()


def print_grid():
    for row in grid:
        print("".join(row))


def move():
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in "^<>v":
                seen.add((r, c))
                if char == "^":
                    if r == 0:
                        grid[r][c] = "."
                    elif grid[r - 1][c] == "#":
                        grid[r][c] = ">"
                    else:
                        grid[r - 1][c] = "^"
                        grid[r][c] = "."
                elif char == ">":
                    if c == len(row) - 1:
                        grid[r][c] = "."
                    elif grid[r][c + 1] == "#":
                        grid[r][c] = "v"
                    else:
                        grid[r][c + 1] = ">"
                        grid[r][c] = "."
                elif char == "v":
                    if r == len(grid) - 1:
                        grid[r][c] = "."
                    elif grid[r + 1][c] == "#":
                        grid[r][c] = "<"
                    else:
                        grid[r + 1][c] = "v"
                        grid[r][c] = "."
                elif char == "<":
                    if c == 0:
                        grid[r][c] = "."
                    elif grid[r][c - 1] == "#":
                        grid[r][c] = "^"
                    else:
                        grid[r][c - 1] = "<"
                        grid[r][c] = "."


while any(char in row for row in grid for char in "^<>v"):
    move()

print(len(seen))
