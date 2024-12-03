f = open("input.txt", "r")
lines = f.read().splitlines()
num_safe = 0

def test_report(report, is_unsafe):
    if report[0] < report[1]:
        for i in range(len(report) - 1):
            if report[i+1] - report[i] < 1 or report[i+1] - report[i] > 3:
                if is_unsafe:
                    return False
                else:
                    is_unsafe = True
    elif report[0] > report[1]:
        for i in range(len(report) - 1):
            if report[i] - report[i+1] < 1 or report[i] - report[i+1] > 3:
                if is_unsafe:
                    return False
                else:
                    is_unsafe = True
    else:
        if not test_report(report[1:], True) and not test_report([report[0]] + report[2:], True):
            return False
    
    return True


for line in lines:
    report = line.split(" ")
    report = [ int(level) for level in report ]
    
    if test_report(report, False):
        num_safe += 1


print(num_safe)