f = open("input.txt", "r")
text = f.read().splitlines()

def get_cost(turn):
    for i in range(100, 0, -1):
        x_from_b = turn[2][0] - (turn[1][0] * i)        
        y_from_b = turn[2][1] - (turn[1][1] * i)
        if x_from_b % turn[0][0] == 0 and y_from_b % turn[0][1] == 0:
            if x_from_b // turn[0][0] == y_from_b // turn[0][1]:
                cost = (x_from_b // turn[0][0]) * 3 + i
                return cost
    return 0

# Read input into array of buttons and prizes
machines = []
machine = []
for line in text:
    steps = len(machine)
    if line == "":
        machines.append(machine)
        machine = []
    elif steps == 0:
        parts = line.split("Button A: X+")[1].split(", Y+")
        machine.append([int(part) for part in parts])
    elif steps == 1:
        parts = line.split("Button B: X+")[1].split(", Y+")
        machine.append([int(part) for part in parts])
    elif steps == 2:
        parts = line.split("Prize: X=")[1].split(", Y=")
        machine.append([int(part) for part in parts])
machines.append(machine)

turn = machines[0]

sum = 0
for machine in machines:
    sum += get_cost(machine)

print(sum)