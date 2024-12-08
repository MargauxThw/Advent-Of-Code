f = open("input.txt", "r")
text = f.read().splitlines()

antinodes = set()
antennas = {}
x_bound = len(text[0])
y_bound = len(text)


def is_in_bounds(tuple):
    if tuple[0] < y_bound and tuple[0] >= 0:
        if tuple[1] < x_bound and tuple[1] >= 0:
            return True
    return False


def get_antinodes(coord, main_coords):
    new_nodes = set()
    coords = []
    coords += main_coords
    coords.remove(coord)
    
    for c in coords:
        vert_dist = coord[0] - c[0]
        hor_dist = coord[1] - c[1]
        
        anti = (coord[0] + vert_dist, coord[1] + hor_dist)
        if is_in_bounds(anti):
            new_nodes.add(anti)
            
        anti = (c[0] - vert_dist, c[1] - hor_dist)
        if is_in_bounds(anti):
            new_nodes.add(anti)
            
    return new_nodes


# Get all antenna locations
for y in range(len(text)):
    for x in range(len(text[y])):
        if text[y][x] != ".":
            if text[y][x] in antennas.keys():
                antennas[text[y][x]].append((y, x))
            else:
                antennas[text[y][x]] =[(y, x)]


# Get all antinodes
for key in antennas.keys():
    if len(antennas[key]) == 1:
        continue
    
    for coord in antennas[key]:
        new_antis = get_antinodes(coord, antennas[key])
        antinodes.update(new_antis)

print(len(antinodes))