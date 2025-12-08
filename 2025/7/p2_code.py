f = open("input.txt", "r")
# f = open("test_input.txt", "r")
rows = f.read().splitlines()

splits = []
for r in range(0, len(rows)):
    splits.append([])
    for ind in range(len(rows[r])):
        if rows[r][ind] == ".":
            if r == 1 and rows[0][ind] == "S":
                splits[r].append(1)
            else:
                splits[r].append(0)
        else:
            splits[r].append(rows[r][ind])

for y in range(2, len(splits)):
    for x in range(len(splits[y])):
        if splits[y][x] != "^":
            if splits[y - 1][x] != "^":
                splits[y][x] += splits[y - 1][x]
            if x != 0 and splits[y - 1][x - 1] == "^":
                splits[y][x] += splits[y - 2][x - 1]
            if x < len(splits[y]) - 1 and splits[y - 1][x + 1] == "^":
                splits[y][x] += splits[y - 2][x + 1]

total = 0
for split in splits[len(splits) - 1]:
    total += split
print(splits)
print(total)
# In the end, print the sum of all the bottom row
# def get_possible_splits(beams, row):
#     if "S" in row or "^" not in row:
#         return (beams, 0)
    
#     splits = 0
#     for r in range(len(row)):
#         if r in beams and row[r] == "^":
#             splits += 1
#             if r - 1 not in beams:
#                 beams.add(r - 1)
#             if r + 1 not in beams:
#                 beams.add(r + 1)
#             beams.discard(r)
    
#     return (beams, splits)

# def get_timelines(beam, row):
#     print(f"beam: {beam}")
#     if row[beam] == "^":
#         return ([beam - 1, beam + 1], 2)
#     else:
#         return ([beam], 0)


# total = 0
# possible_routes = {0: [rows[0].index("S")]}

# for r in range(2, len(rows), 2):
#     for route in possible_routes[r - 2]:
#         # print(possible_routes[r], route, r)
#         possible_routes[r] = []
#         print(f"Route: {route} in {possible_routes[r - 2]}")
#         result = get_timelines(route, rows[r])
#         print(f"result: {result}")
#         total += result[1]
#         possible_routes[r] += result[0]
        # for path in route:

# print(total)