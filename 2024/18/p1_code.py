import time
start_time = time.time()

f = open("input.txt")
text = f.read().splitlines()

bound = 70

grid = [["." for i in range(0, bound + 1)] for i in range(0, bound + 1)]

for line in range(0, 1024):
    coords = [int(j) for j in text[line].split(",")]
    grid[coords[1]][coords[0]] = "X"

# for y in grid:
#     print("".join(str(y)))


def get_adj(y, x):
    adj = []
    if y > 0:
        adj.append((y - 1, x))
    if y < bound:
        adj.append((y + 1, x))
    if x > 0:
        adj.append((y, x - 1))
    if x < bound:
        adj.append((y, x + 1))
        
    return adj

explored = []
queue = [[(0, 0)]]

while queue:
    path = queue.pop(0)
    node = path[-1]
    
    if node not in explored:
        neighbours = get_adj(node[0], node[1])
    
        for neighbour in neighbours:
            if grid[neighbour[0]][neighbour[1]] != "X" and neighbour not in path:
                new_path = path.copy()
                new_path.append(neighbour)
                queue.append(new_path)
            
                if neighbour == (bound, bound):
                    print(len(new_path) - 1)
                    print("--- %s seconds ---" % (time.time() - start_time))
                    exit()
                    
        explored.append(node)

print("--- %s seconds ---" % (time.time() - start_time))