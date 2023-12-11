from collections import deque # doubly ended queue

grid = open(0).read().strip().splitlines()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break

# set for seen to make sure we dont visit twice and for length
seen = {(sr, sc)}
# queue to make sure we scan nodes in orderly fashion
q = deque([(sr, sc)])

while q:
    r, c = q.popleft()
    ch = grid[r][c]
    # check every direction, using possible movement chars
    if r > 0 and ch in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in seen:
        seen.add((r - 1, c))
        q.append((r - 1, c))

    if r < len(grid) - 1 and ch in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in seen:
        seen.add((r + 1, c))
        q.append((r + 1, c))

    if c > 0 and ch in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in seen:
        seen.add((r, c - 1))
        q.append((r, c - 1))

    if c < len(grid[r]) - 1 and ch in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in seen:
        seen.add((r, c + 1))
        q.append((r, c + 1))

print(len(seen) // 2)