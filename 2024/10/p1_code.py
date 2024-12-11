from collections import deque

f = open("input.txt", "r")
text = f.read().splitlines()

last_x = len(text[0]) - 1
last_y = len(text) - 1

score = 0

def get_paths(src):
    paths = []
    ends = []
    q = deque()
    
    path = []
    path.append(src)
    q.append(path.copy())
    
    while q:
        path = q.popleft()
        y, x = path[len(path) - 1][0], path[len(path) - 1][1]
        last = int(text[y][x])
        
        if int(last) == 9 and (y, x) not in ends:
            paths.append(path)
            ends.append((y, x))
        
        new_steps = set()
        if y != 0 and last + 1 == int(text[y-1][x]): # above
            new_steps.add((y - 1, x))
            
        if x < last_x and last + 1 == int(text[y][x + 1]): # right
            new_steps.add((y, x + 1))
        
        if y < last_y and last + 1 == int(text[y + 1][x]):
            new_steps.add((y + 1, x))
        
        if x > 0 and last + 1 == int(text[y][x - 1]):
            new_steps.add((y, x - 1))
            
        for step in new_steps:
            new_path = path.copy()
            new_path.append((step[0], step[1]))
            q.append(new_path)

    return len(paths)

for y in range(len(text)):
    for x in range(len(text[y])):
        if int(text[y][x]) == 0:
            score += get_paths((y, x))

print(score)