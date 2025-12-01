f = open("test_2.txt", "r")
text = f.read().splitlines()

dirs = [">", "v", "<", "^"]
S = ()
E = ()

graph = {}
for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x] == "." or text[y][x] == "S" or text[y][x] == "E":
            graph[(y, x)] = {}
            if y > 0 and text[y - 1][x] in ".SE":  # up
                graph[(y, x)][dirs[3]] = (y - 1, x)
            if x < len(text[y]) - 1 and text[y][x + 1] in ".SE":  # right
                graph[(y, x)][dirs[0]] = (y, x + 1)
            if y < len(text) - 1 and text[y + 1][x] in ".SE":  # down
                graph[(y, x)][dirs[1]] = (y + 1, x)
            if x > 0 and text[y][x - 1] in ".SE":  # left
                graph[(y, x)][dirs[2]] = (y, x - 1)

        if text[y][x] == "E":
            E = (y, x)

        if text[y][x] == "S":
            S = (y, x)

def calculate_cost(current_dir, next_dir, steps):
    current_index = dirs.index(current_dir)
    next_index = dirs.index(next_dir)
    turn_cost = 0
    if current_index != next_index:
        if (current_index == 0 and next_index == 3) or (current_index == 3 and next_index == 0):
                turn_cost += 1000
        elif current_index > next_index:
            turn_cost += 1000 * (current_index - next_index)
        else:
            turn_cost += 1000 * (next_index - current_index)
    # turn_cost = abs(next_index - current_index) * 1000
    print(turn_cost, current_dir, next_dir)
    # if abs(next_index - current_index) == 3:  # Handle wrap-around case (e.g., from '^' to '>')
    #     turn_cost = 1000
    return steps + turn_cost

def get_all_optimal_paths(source, target, graph):
    from collections import deque, defaultdict

    queue = deque([(source, [source], ">", 0)])  # Start facing right with cost 0
    visited = defaultdict(lambda: float('inf'))
    visited[(source, ">")] = 0
    optimal_paths = []
    lowest_cost = float('inf')

    while queue:
        current, path, current_dir, cost = queue.popleft()

        if current == target:
            if cost < lowest_cost:
                lowest_cost = cost
                optimal_paths = [path]
            elif cost == lowest_cost:
                optimal_paths.append(path)
            continue

        for next_dir in graph[current]:
            neighbor = graph[current][next_dir]
            step_cost = calculate_cost(current_dir, next_dir, 1)
            new_cost = cost + step_cost

            if new_cost < visited[(neighbor, next_dir)]:
                visited[(neighbor, next_dir)] = new_cost
                queue.append((neighbor, path + [neighbor], next_dir, new_cost))

    return optimal_paths

# Get all optimal paths
optimal_paths = get_all_optimal_paths(S, E, graph)

# Compute the union of all coordinates visited in optimal paths
unique_coordinates = set()
for path in optimal_paths:
    unique_coordinates.update(path)

print(len(unique_coordinates))


new_text = []
for y in range(len(text)):
    new_text.append("")
    for x in range(len(text[y])):
        if (y, x) in unique_coordinates:
            new_text[y] += "O"
        else:
            new_text[y] += text[y][x]

for y in range(len(new_text)):
    print("".join(new_text[y]))

# too low: 489