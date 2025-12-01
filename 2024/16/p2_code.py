import functools
import time
start_time = time.time()

f = open("test_1.txt", "r")
text = f.read().splitlines()

dirs = [">", "v", "<", "^"]
S = ()
E = ()
dir = 0

graph = {}
for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x] == "." or text[y][x] == "S" or text[y][x] == "E":
            graph[(y, x)] = {}
            if text[y - 1][x] in ".SE": # up
                graph[(y, x)][dirs[3]] = (y - 1, x)
            if text[y][x + 1] in ".SE": # right
                graph[(y, x)][dirs[0]] = (y, x + 1)
            if text[y + 1][x] in ".SE": # down
                graph[(y, x)][dirs[1]] = (y + 1, x)
            if text[y][x - 1] in ".SE": # left
                graph[(y, x)][dirs[2]] = (y, x - 1)
        
        if text[y][x] == "E":
            E = (y, x)
        
        if text[y][x] == "S":
            S = (y, x)

def get_paths(source, graph):
    unvisited = [key for key in graph.keys()]
    distances = {source: [0, ">"]}
    paths = {}
    
    for key in unvisited:
        if key != source:
            distances[key] = [float("inf"), None]
        paths[key] = set()
    
    temp_node = source
    while len(unvisited) != 0:
        unvisited.remove(temp_node)
        
        for dir in graph[temp_node]:
            if graph[temp_node][dir] in unvisited:
                temp = distances[graph[temp_node][dir]].copy()
                temp[0] = distances[temp_node][0] + 1
                
                temp[1] = dir
                if distances[temp_node][1] != temp[1]:
                    parent_dir = dirs.index(distances[temp_node][1])
                    child_dir = dirs.index(temp[1])
                    
                    if (child_dir == 0 and parent_dir == 3) or (child_dir == 3 and parent_dir == 0):
                        temp[0] += 1000
                    elif child_dir > parent_dir:
                        temp[0] += 1000 * (child_dir - parent_dir)
                    else:
                        temp[0] += 1000 * (parent_dir - child_dir)
            
            if temp[0] < distances[graph[temp_node][dir]][0]:
                distances[graph[temp_node][dir]] = temp.copy()
                paths[graph[temp_node][dir]] = paths[temp_node].copy()
                paths[graph[temp_node][dir]].add(temp_node)
        
        lowest = float("inf")
        for key in unvisited:
            if distances[key][0] <= lowest:
                lowest = distances[key][0]
                temp_node = key
        
    return distances, paths

@functools.lru_cache(None)
def get_cost(path, boundary, start_dir):
    path = [[p, ""] for p in path]
    path[0][1] = start_dir
    
    cost = 0
    for i in range(1, len(path)):
        cost += 1
        if path[i - 1][0][0] == path[i][0][0]: # same y
            if path[i - 1][0][1] > path[i][0][1]:
                temp_dir = ">"
            else:
                temp_dir = "<"
        else:
            if path[i - 1][0][0] > path[i][0][0]:
                temp_dir = "^"
            else:
                temp_dir = "v"
        
        prev_dir = dirs.index(path[i - 1][1])
        new_dir = dirs.index(temp_dir)
        path[i][1] = temp_dir
        
        if new_dir != prev_dir:
            if (new_dir == 0 and prev_dir == 3) or (new_dir == 3 and prev_dir == 0):
                    cost += 1000
            elif new_dir > prev_dir:
                cost += 1000 * (new_dir - prev_dir)
            else:
                cost += 1000 * (prev_dir - new_dir)
        
        if cost > boundary:
            return -1
    
    return cost

def get_all_paths(source, target, start_dir, boundary):
    queue = [[source]]
    true_paths = []
    # boundary = 99488
    
    while len(queue) > 0:
        # print(len(queue))
        path = queue.pop()
        if path[len(path) - 1] == target:
            cost = get_cost(tuple(path), boundary, start_dir)
            print(cost)
            if cost > -1:
                if cost > boundary:
                    print("TOO BIG")
                    continue
                if cost < boundary:
                    boundary = cost
                    for true_path in true_paths:
                        print(true_path[1])
                        if true_path[1] > boundary:
                            print("REMOVING", true_path)
                            true_paths.remove(true_path)
                true_paths.append((path, cost))
            continue
        for dir in graph[path[len(path) - 1]]:
            if graph[path[len(path) - 1]][dir] not in path:
                new_path = path.copy()
                new_path.append(graph[path[len(path) - 1]][dir])
                
                # cost = get_cost(tuple(new_path), boundary, start_dir)
                # if cost == -1:
                #     print("TOO MUCH COST")
                #     continue
                # print("COST OK", cost)
                
                queue.append(new_path)
        
    return true_paths
            
distances, keys = get_paths(S, graph)
print(keys[E])
keys = [k for k in keys[E]]
# keys = [key for key in distances.keys()]

for i in range(len(distances) - 2):
    print(distances[keys[i]])
    
    for j in range(i + 2, len(distances)):
        print(keys[i], keys[j], distances[keys[i]][1])
        print(get_all_paths(keys[i], keys[j], distances[keys[i]][1], distances[keys[j]][0] - distances[keys[i]][0]))

# all_paths = get_all_paths(S, E)
# all_nodes = set()
# for path in all_paths:
#     all_nodes.update(path[0])

# print(len(all_nodes))

print("--- %s seconds ---" % (time.time() - start_time))
