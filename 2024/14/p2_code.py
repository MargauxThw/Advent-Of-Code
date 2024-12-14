f = open("input.txt", "r")
text = f.read().splitlines()

x_bound = 101
y_bound = 103
time = 100

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

print(i)