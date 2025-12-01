f = open("input.txt", "r")
lines = f.read().splitlines()

num_zeros = 0
current_dial = 50

for full_line in lines:
    dir = full_line[0]
    turn = int(full_line[1:])
    
    counter = 0
    if dir == 'R':
        while counter < turn:
            current_dial += 1
            if current_dial == 100:
                current_dial = 0
                
            if current_dial == 0:
                num_zeros += 1
            
            counter += 1
    else:
        while counter < turn:
            current_dial -= 1
            if current_dial == -1:
                current_dial = 99
            elif current_dial == 0:
                num_zeros += 1
            
            counter += 1

print(num_zeros)