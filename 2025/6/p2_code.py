f = open("input.txt", "r")
# f = open("test_input.txt", "r")
rows = f.read().splitlines()

eqs = []
starts = []
for col in range(len(rows[0])):
    if rows[len(rows) - 1][col] != " ":
        starts.append(int(col))

for i in range(len(rows[0])):
    if i in starts:
        new_eq = []
        for row in rows:
            if starts.index(i) == len(starts) - 1:
                new_eq.append(row[i:])
            else:  
                new_eq.append(row[i : starts[starts.index(i) + 1] - 1])
        eqs.append(new_eq)

total = 0
for eq in eqs:
    nums = []
    for i in range(len(eq[0])):
        col_number = ""
        for j in range(len(eq) - 1):
            col_number += eq[j][i]
        # print(col_number, eq)
        if col_number.strip() != "":
            nums.append(int(col_number.strip()))
    
    sub_total = nums[0]
    add = "+" in eq[len(eq) - 1]
    for val in nums[1:]:
        if add:
            sub_total += val
        else:
            sub_total *= val
    total += sub_total
    
print(total)