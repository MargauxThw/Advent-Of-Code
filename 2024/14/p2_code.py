f = open("input.txt", "r")
text = f.read().splitlines()

x_bound = 101
y_bound = 103
time = 100

def visualise_robots(pos, i):
    print(str(i) + ":")
    map = [["" for x in range(x_bound)] for y in range(y_bound)]
    for y in range(y_bound):
        for x in range(x_bound):
            # if x == x_bound // 2 or y == y_bound // 2:
            #     map[y][x] = " "
            if (x, y) in pos:
                map[y][x] = "*"
            else:
                map[y][x] = "."
        print("".join(map[y]))

i = -1
new_ends = set()
while len(new_ends) != len(text):
    i += 1
    new_ends = set()
    for line in text:
        pos = [int(x) for x in line.split("p=")[1].split(" v=")[0].split(",")]
        vel = [int(x) for x in line.split("p=")[1].split(" v=")[1].split(",")]
        x_final = (pos[0] + vel[0] * i) % x_bound
        y_final = (pos[1] + vel[1] * i) % y_bound
        new_ends.add((x_final, y_final))
    # visualise_robots(new_ends, i)

print(i)