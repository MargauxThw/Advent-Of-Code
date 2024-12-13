f = open("input.txt", "r")
map = f.read().splitlines()

def get_regions(boxes):
    if len(boxes) == 1:
        return boxes
    
    regions = []
    
    for box in boxes:
        y, x = box[0], box[1]
        is_added = False
        added = -1
        for region_index in range(len(regions)):
            if any(b in regions[region_index] for b in [[y, x+1], [y, x-1], [y-1, x], [y+1, x]]):
                if not is_added:
                    regions[region_index].append([y, x])
                    is_added = True
                    added = region_index
                else:
                    regions[added].extend(regions[region_index])
                    regions[region_index] = []
                    
                
        if not is_added:
            regions.append([[y, x]])
        
    return regions

def get_sides(edges):
    sides = 0
    for side in edges.keys():
        if len(edges[side]) == 1:
            sides += 1
            continue
        
        if side in ["T", "B"]:
            rows = {}
            for edge in edges[side]:
                y, x = edge[0], edge[1]
                if y in rows.keys():
                    rows[y].append(edge)
                else:
                    rows[y] = [edge]
            for row in rows:
                this_row = sorted(rows[row])
                ptr = 0
                sides += 1
                while ptr < len(this_row) - 1:
                    if this_row[ptr + 1][1] - this_row[ptr][1] > 1:
                        sides += 1
                        
                    ptr += 1
        
        else:
            cols = {}
            for edge in edges[side]:
                y, x = edge[0], edge[1]
                if x in cols.keys():
                    cols[x].append(edge)
                else:
                    cols[x] = [edge]
            for col in cols:
                this_col = sorted(cols[col])
                ptr = 0
                sides += 1
                while ptr < len(this_col) - 1:
                    if this_col[ptr + 1][0] - this_col[ptr][0] > 1:
                        sides += 1
                    ptr += 1

    return sides

squares = {}
for y in range(len(map)):
    for x in range(len(map[y])):
        this_square = map[y][x]
        if this_square in squares.keys():
            squares[this_square].append([y, x])
            
        else:
            squares[this_square] = [[y, x]]

regions = []
for plant in squares.keys():
    new_regions = get_regions(squares[plant])
    if len(new_regions[0]) > 1 and type(new_regions[0][0]) is list:
        for region in new_regions:
            if region != []:
                regions.append(region)
    else:
        regions.extend(new_regions)

sum = 0
for region in regions:
    if region == []:
        continue
    
    region_sum = 0
    edges = {"T": [], "R": [], "B": [], "L": []}
    
    if len(region) == 1:
        sum += 4
        continue
    
    if type(region[0]) is int:
        region = [region]
    
    for box in region:
        y, x = box[0], box[1]
        if [y - 1, x] not in region:
            region_sum += 1
            edges["T"].append([y, x])
        if [y, x + 1] not in region:
            region_sum += 1
            edges["R"].append([y, x])
        if [y + 1, x] not in region:
            region_sum += 1
            edges["B"].append([y, x])
        if [y, x - 1] not in region:
            region_sum += 1
            edges["L"].append([y, x])
        
    sum += get_sides(edges) * len(region)
        
print(sum)