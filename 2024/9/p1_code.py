f = open("input.txt", "r")
text = f.read()

# Get step 1 - before moving
system = []
for i in range(len(text)):
    if i % 2 == 0: # File case
        for j in range(int(text[i])):
            system.append(str(int(i // 2)))
    else: # Space case
        for j in range(int(text[i])):
            system.append(".")

start = 0
end = len(system) - 1

# Transform array
while start < end:
    while system[start] != ".":
        start += 1
    while system[end] == ".":
        end -= 1

    system[start] = system[end]
    system[end] = "."
    
    start += 1
    end -= 1

# Find checksum
checksum = 0
for i in range(len(system)):
    if system[i] != ".":
        break
    checksum += (i * int(system[i]))
    
print(checksum)