f = open("input.txt", "r")
text = f.read()

# Get sections that are allowed
valid_sections = []
is_restricted = True
restrictions = text.split("do")
for i in range(len(restrictions)):
    if restrictions[i][:5] == "n't()":
        is_restricted = True
    elif restrictions[i][:2] == "()" or i == 0 or not is_restricted:
        is_restricted = False
        valid_sections.append(restrictions[i])

# Adapt solution from part one below
sections = []

for section in valid_sections:
    parts = section.split("m")
    sections += parts

total = 0

for section in sections:
    # Check for an end
    sub_section = section.split(")")[0]
    if len(sub_section) == len(section):
        continue
    
    # Check for a valid start
    if not sub_section[:3] == "ul(":
        continue
    
    # Remove valid start and check for 2 params (nums)
    nums = sub_section[3:].split(",")
    if len(nums) != 2 or " " in nums[0] or " " in nums[1]:
        continue
    
    # Check params are valid ints
    try:
        num_1 = int(nums[0])
        num_2 = int(nums[1])
    except:
        continue
    
    if num_1 > 999 or num_2 > 999:
        continue
    
    # Success: Add product to total
    total += num_1 * num_2


print(total)