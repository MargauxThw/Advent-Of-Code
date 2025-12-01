f = open("input.txt", "r")
lines = f.read().splitlines()

num_zeros = 0
current_dial = 50

for full_line in lines:
    dir = full_line[0]
    turn = int(full_line[1:])
    
    if dir == 'R':
        current_dial += turn
    else:
        current_dial -= turn
    
    current_dial %= 100
    
    if current_dial == 0:
        num_zeros += 1
    

print(num_zeros)