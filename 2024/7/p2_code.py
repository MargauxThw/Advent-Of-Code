def get_possible_ans(next_num, current_ans):
    new_possible_ans = set()
    # Get the new variations based on all previous variations
    for ans in current_ans:
        new_possible_ans.add(ans * next_num)
        new_possible_ans.add(ans + next_num)
        # Edit for part 2 - additional possible operation
        new_possible_ans.add(int(str(ans) + str(next_num)))
    return new_possible_ans

f = open("input.txt", "r")
text = f.read().splitlines()

total = 0

for line in text:
    target = int(line.split(":")[0])
    nums = [int(x) for x in line.split(":")[1].split(" ")[1:]]
    new_ans = [nums[0]]
    # Do permutations for all numbers in list
    for num in range(len(nums)):
        if num == 0:
            continue
        new_ans = get_possible_ans(nums[num], new_ans)
    # Have cycled through all, now check final results
    if target in new_ans:
        total += target
    
print(total)