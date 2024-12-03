


def parse_input(input_data):
    arr = []

    lines = input_data.splitlines()

    for line in lines:
        line = line.split(' ')
        line = [int(i) for i in line] # cast strings to int
        
        arr.append(line)
    return arr

def get_safe_count(reports):
    count = 0

    for report in reports:
        if isSafe(report):
            count += 1
        elif isSafeWithDampener(report):
            count += 1
    
    return count


def isSafe(report):
        isIncrease = False
        isDecrease = False

        if len(report) == 1:
             return True
        
        if report[0] < report[-1]:
             isIncrease = True
        else:
             isDecrease = True
        
        if isIncrease:
            for i in range(len(report) - 1):
                if report[i] >= report[i+1] or report[i+1] - report[i] > 3:
                     return False
        if isDecrease:
            for i in range(len(report) - 1):
                if report[i] <= report[i+1] or report[i] - report[i+1] > 3:
                     return False
        
        return True


def isSafeWithDampener(report):
    cur_report = []

    for i in range(len(report)):
        cur_report = copy_arr(report)
        cur_report.pop(i)
        

        if isSafe(cur_report):
            return True
    
    return False


def copy_arr(arr):
    copy = []
    for i in range(len(arr)):
        copy.append(arr[i])
    return copy
