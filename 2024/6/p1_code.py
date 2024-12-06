f = open("input.txt", "r")
map = f.read().splitlines()


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # [UP, LEFT, DOWN, RIGHT]
dir = 0 # index in dirs array for current direction
pos = (0,0) # elf position
row_bound = len(map)
col_bound = len(map[0])


# Get starting pos and dir
for row in range(len(map)):
    if "^" in map[row]:
        dir = 0
        pos = (row, map[row].index("^"))
    elif ">" in map[row]:
        dir = 1
        pos = (row, map[row].index(">"))
    elif "v" in map[row]:
        dir = 2
        pos = (row, map[row].index("^"))
    elif "<" in map[row]:
        dir = 3
        pos = (row, map[row].index("^"))

# Initialise set of unique squares visited
visited = set()   
visited.add(pos)

# If the elf is in bounds, run movement loop
while pos[0] < row_bound and pos[0] >= 0 and pos[1] < col_bound and pos[1] >= 0:
    test_next = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
    
    if test_next[1] == col_bound or test_next[0] == row_bound:
        break
    
    if map[test_next[0]][test_next[1]] == "#":
        # Turn if hitting an obstacle
        dir = (dir + 1) % 4
    else:
        # Move to next move (if not an obstacle)
        visited.add(test_next)
        pos = test_next

print(len(visited))