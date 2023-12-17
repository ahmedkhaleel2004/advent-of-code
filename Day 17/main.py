from heapq import heappush, heappop

# we will use djikstras

grid = [list(map(int, line.strip())) for line in open(0)]

seen = set()
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)
    
    if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4: # make sure we moved 4 before stopping
        print(hl) # first time we see end position, hl will be smallest value
        break

    if (r, c, dr, dc, n) in seen: # hl not included to not get stuck in loop
        continue

    seen.add((r, c, dr, dc, n))
    
    if n < 10 and (dr, dc) != (0, 0): # update 3 to 10
        nr = r + dr
        nc = c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

    if n >= 4 or (dr, dc) == (0, 0): # make sure we moved at least 4 or stopped before trying to turn
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))