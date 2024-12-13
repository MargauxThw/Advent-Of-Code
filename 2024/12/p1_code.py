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
    # if region == []:
    #     continue
    
    region_sum = 0
    
    # if len(region) == 1:
    #     sum += 4
    #     continue
    
    for box in region:
        if [box[0] - 1, box[1]] not in region:
            region_sum += 1
        if [box[0], box[1] + 1] not in region:
            region_sum += 1
        if [box[0] + 1, box[1]] not in region:
            region_sum += 1
        if [box[0], box[1] - 1] not in region:
            region_sum += 1
    sum += region_sum * len(region)
        
print(sum)