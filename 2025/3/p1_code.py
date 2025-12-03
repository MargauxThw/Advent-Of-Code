f = open("input.txt", "r")
banks = f.read().splitlines()

total_output = 0

for bank in banks:
    highest_left = 0
    highest_left_i = 0
    for i in range(0, len(bank) - 1):
        if int(bank[i]) > highest_left:
            highest_left = int(bank[i])
            highest_left_i = i

    highest_right = int(bank[i + 1])
    highest_right_i = highest_left_i + 1
    for i in range(highest_right_i, len(bank)):
        if int(bank[i]) > highest_right:
            highest_right = int(bank[i])
            highest_right_i = i

    total_output += int(str(highest_left) + str(highest_right))

print(total_output)