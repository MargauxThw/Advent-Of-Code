f = open("input.txt", "r")
lines = f.read().splitlines()

num_safe = 0
asc = True


for line in lines:
    report = line.split(" ")
    report = [ int(level) for level in report ]
    safe = True
    
    if report[0] < report[1]:
        for i in range(len(report) - 1):
            if report[i+1] - report[i] < 1 or report[i+1] - report[i] > 3:
                safe = False
    elif report[0] > report[1]:
        for i in range(len(report) - 1):
            if report[i] - report[i+1] < 1 or report[i] - report[i+1] > 3:
                safe = False
    else:
        safe = False
    
    if safe:
        num_safe += 1
    
print(num_safe)