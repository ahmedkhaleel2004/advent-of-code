grid = open(0).read().splitlines()

grid = list(map("".join, zip(*grid))) # transposed rows is easier to work with here so we dont have to deal with cols

# for each row, separate by the groups (blocked by #), sort the string in reverse, join it again using #
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]

# transpose back
grid = list(map("".join, zip(*grid)))

# count "O" * idx in each row
print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))