f = open("input.txt", "r")
banks = f.read().splitlines()

total_output = 0

for bank in banks:
    final = ""
    values = []
    while len(final) < 12:
        x = 0
        y = len(bank) - 11

        if len(values) != 0:
            x = values[len(values) - 1][0] + 1
            y += len(final)
        
        max = (0, 0)
        for i in range(x, y):
            if int(bank[i]) > max[1]:
                max = (i, int(bank[i]))

        final += str(max[1])
        values.append(max)

    total_output += int(final)

print(total_output)

# Method - find the smallest len - 12 digits and turn off left to right?? doesn't work for 234234234234278 though
# Another method - find the left-most highest number until you run out of cancels. Repeat starting from l_index + 1, etc.
### But if there's one of same value that's been skipped, go back to that
# Another: Find the first number. Find the lowest with one heigher after & remove. Repeat this until you've removed the remaining limit
# Final: Edge cases, use a window don't go all the way to the end - focus on finding the next digit, and build from there