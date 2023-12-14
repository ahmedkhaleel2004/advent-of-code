grid = tuple(open(0).read().splitlines())

def cycle():
    global grid # modify grid in place
    for _ in range(4):
        # tuples to put into seen set

        # so we can tilt to each side by keeping the shift logic
        # but changing the direction of the grid in place
        # much easier this way
        # therefore, to rotate clockwise
        # you can take the transpose and reverse the rows
        # for a 90 deg turn clockwise
        
        # transpose
        grid = tuple(map("".join, zip(*grid))) 
        # for each row, separate by the groups (blocked by #), sort the string in reverse, join it again using #
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        # reverse rows
        grid = tuple(row[::-1] for row in grid)

# eventually it will catch onto a cycle with a billion iterations
# therefore we can just catch the index of where it starts cycling
# and use this to modulo 1 billion to return the state + the offset for our start

seen = {grid}
array = [grid]

iter = 0

while True:
    iter += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)
    
first = array.index(grid)

grid = array[(1000000000 - first) % (iter - first) + first]

# count "O" * idx in each row
print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))