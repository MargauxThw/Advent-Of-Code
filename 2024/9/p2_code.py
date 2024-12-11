f = open("input.txt", "r")
text = f.read()

# Get step 1 - before moving
system = []
starting_index = 0
for i in range(len(text)):
    if i % 2 == 0: # File case
        # Append [value, size, starting_index]
        system.append([str(int(i // 2)), int(text[i]), starting_index])
    starting_index += int(text[i])

total_length = starting_index

to_move = len(system) - 1
while to_move > 0:
    to_land_after = 0
    space_needed = system[to_move][1]
    moved = False
    while to_land_after < to_move:
        space_available = system[to_land_after + 1][2] - (system[to_land_after][2] + system[to_land_after][1])
        if space_available >= space_needed:
            system[to_move][2] = system[to_land_after][2] + system[to_land_after][1]
            system = sorted(system, key = lambda x: x[2])
            moved = True
            break
        else:
            to_land_after += 1
    
    if not moved:
        to_move -= 1

# Put the spaces back
s = []
for item in range(len(system)):        
    if item == 0 and system[item][2] != 0:
        for i in range(system[item][2]):
            s += "."
            
    for i in range(system[item][1]):
        s.append(system[item][0])
        
    if item < len(system) - 1 and system[item][1] + system[item][2] != system[item + 1][2]:
        for i in range(system[item + 1][2] - (system[item][1] + system[item][2])):
            s += "."

# Find checksum
checksum = 0
for i in range(len(s)):
    if s[i] != ".":
        checksum += i * int(s[i])

print(checksum)