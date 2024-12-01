# go through rows and transpose for cols

def find_mirror(grid):
    for r in range(1, len(grid)):
        # above and below, to the size of the smaller, while flipping above strictly
        above = grid[:r][::-1]
        below = grid[r:]
        
        above = above[:len(below)]
        below = below[:len(above)]
        
        # part 2: simply change condition to iterate through number of errors in above and below and return row idx of strictly 1 error
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r
        
    return 0

total = 0

for block in open(0).read().split("\n\n"):
    grid = block.splitlines()

    row = find_mirror(grid)
    total += row * 100

    col = find_mirror(list(zip(*grid))) # transpose
    total += col

print(total)