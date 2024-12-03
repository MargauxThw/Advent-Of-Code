f = open("input.txt", "r")
lines = f.read().splitlines()

list_1 = set()
list_2 = []

for line in lines:
    nums = line.split("   ")
    list_1.add(int(nums[0]))
    list_2.append(int(nums[1]))

sim_dict = dict.fromkeys((list_1), 0)

for i in range(len(list_2)):
    if list_2[i] in list_1:
        sim_dict[list_2[i]] += 1
    
total_sim = 0    

for item in list_1:
    total_sim += sim_dict[item] * item
    
print(total_sim)