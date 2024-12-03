f = open("input.txt", "r")
lines = f.read().splitlines()

list_1 = []
list_2 = []

for line in lines:
    nums = line.split("   ")
    list_1.append(int(nums[0]))
    list_2.append(int(nums[1]))

list_1.sort()
list_2.sort()


total = 0
for i in range(len(list_1)):
    dist = list_1[i] - list_2[i]
    if dist < 0:
        dist *= -1
    total += dist
    
print(total)