f = open("input.txt", "r")
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

distances, paths = get_paths(S, graph)
print(distances[E])
# print(paths[E])


new_text = []
for y in range(len(text)):
    new_text.append("")
    for x in range(len(text[y])):
        if (y, x) in paths[E]:
            new_text[y] += "X"
        else:
            new_text[y] += text[y][x]


# for y in range(len(new_text)):
#     print("".join(new_text[y]))