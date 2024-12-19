import time
start_time = time.time()

f = open("input.txt")
text = f.read().splitlines()

bound = 70

grid = [["." for i in range(0, bound + 1)] for i in range(0, bound + 1)]

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

def get_is_blocked(coords, prev_path):
    if prev_path != [] and (coords[0], coords[1]) not in prev_path:
        return False, prev_path
    
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
                        return False, new_path
                        
            explored.append(node)
    
    return True, None


visited = set()
for line in range(0, 3030):
    coords = [int(j) for j in text[line].split(",")]
    grid[coords[1]][coords[0]] = "X"
    if line == 0:
        is_blocked, prev_path = get_is_blocked(coords, [])
    else:
        if len(set(prev_path).intersection(visited)) > 0:
            is_blocked, prev_path = get_is_blocked(coords, [])
        else:
            is_blocked, prev_path = get_is_blocked(coords, prev_path)
    
    # for y in grid:
    #     print("".join(y))
        
    if is_blocked:
        last_coords = [int(j) for j in text[line - 1].split(",")]
        print(f"{last_coords[0]},{last_coords[1]}")
        break
    
    visited.add((coords[1], coords[0]))

print("--- %s seconds ---" % (time.time() - start_time))