from collections import deque
import time
start_time = time.time()

# f = open("input.txt")
f = open("test_1.txt")
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
cheat_paths = set()
for (x, y), t1 in visited.items():
    for c in range(20):
        for i, j in [(x+c, y), (x-c, y), (x, y-c), (x, y+c)]:
            # if visited.get((i, j), 0) - t1 > 101:
            if visited.get((i, j), 0) - t1 > 51:
                cheats += 1
                print(i, j, c)
                
print(cheats)
print("--- %s seconds ---" % (time.time() - start_time))

# Too low: 9908