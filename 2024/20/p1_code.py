from collections import deque
import time
start_time = time.time()

f = open("input.txt")
grid = f.read().splitlines()

rows, cols = len(grid), len(grid[0])
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == 'S':
            S = (row, col)
        elif grid[row][col] == 'E':
            E = (row, col)
            
queue = deque([(*S, 0, dict())])

while queue:
    x, y, step, visited = queue.popleft()
    visited[(x, y)] = step
    
    if (x, y) == E:
        break

    for i, j in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
        if (i in range(rows) and j in range(cols) and
            (i, j) not in visited and grid[i][j] != '#'):
            queue.append((i, j, step + 1, visited.copy()))


cheats = 0
for (x, y), t1 in visited.items():
    for i, j in [(x+2, y), (x-2, y), (x, y-2), (x, y+2)]:
        if visited.get((i, j), 0) - t1 > 101:
            cheats += 1
                
print(cheats)
print("--- %s seconds ---" % (time.time() - start_time))