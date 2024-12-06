def get_visited():
    pos = orig_pos
    dir = orig_dir
    # Initialise set of unique squares visited
    visited = set()   
    # visited.add(pos)

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
    
    return visited

# Start of main code
f = open("input.txt", "r")
map = f.read().splitlines()

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)] # [UP, LEFT, DOWN, RIGHT]
orig_dir = 0 # index in dirs array for current direction
orig_pos = (0,0) # original elf position
row_bound = len(map)
col_bound = len(map[0])
total = 0

# Get starting pos and dir (initialising)
for row in range(len(map)):
    if "^" in map[row]:
        orig_dir = 0
        orig_pos = (row, map[row].index("^"))
    elif ">" in map[row]:
        orig_dir = 1
        orig_pos = (row, map[row].index(">"))
    elif "v" in map[row]:
        orig_dir = 2
        orig_pos = (row, map[row].index("^"))
    elif "<" in map[row]:
        orig_dir = 3
        orig_pos = (row, map[row].index("^"))

# Check each visited square in case it can cause a loop
for cell in get_visited():
    map[cell[0]] = map[cell[0]][:cell[1]] + "#" + map[cell[0]][cell[1] + 1:]
        
    pos = orig_pos
    dir = orig_dir
    
    # Initialise set of unique squares visited
    visited = set()
    visited.add((pos, dir))

    # If the elf is in bounds, run movement loop
    while pos[0] < row_bound and pos[0] >= 0 and pos[1] < col_bound and pos[1] >= 0:
        test_next = (pos[0] + dirs[dir][0], pos[1] + dirs[dir][1])
        
        if test_next[1] == col_bound or test_next[0] == row_bound:
            break
        
        if map[test_next[0]][test_next[1]] == "#":
            # Turn if hitting an obstacle
            dir = (dir + 1) % 4
        elif (test_next, dir) in visited:
            # Same square, same direction means a loop!
            total += 1
            break
        else:
            # Move to next move (if not an obstacle)
            visited.add((test_next, dir))
            pos = test_next
    
    # Reset map for next loop iteration
    map[cell[0]] = map[cell[0]][:cell[1]] + "." + map[cell[0]][cell[1] + 1:]


print(total)