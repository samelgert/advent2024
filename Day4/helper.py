
def parse_input(input_data):
    arr = []

    lines = input_data.splitlines()

    return lines


def word_search(rows):
    count = 0
    for row in range(len(rows)):
        x_indices = list(find_all(rows[row], 'X'))
        for x in x_indices:
            if x > 2: # Can have word to the left
                if rows[row][x-1] == 'M' and rows[row][x-2] == 'A' and rows[row][x-3] == 'S': # check left side
                    count += 1
            if x < len(rows[row]) - 3: # Can have a word to the right
                if rows[row][x+1] == 'M' and rows[row][x+2] == 'A' and rows[row][x+3] == 'S': # check right side
                    count += 1
            if row > 2: #Can have a word above
                if rows[row-1][x] == 'M' and rows[row-2][x] == 'A' and rows[row-3][x] == 'S': # check above
                    count += 1
                if x > 2: # Can have word to left+up diagonal
                    if rows[row-1][x-1] == 'M' and rows[row-2][x-2] == 'A' and rows[row-3][x-3] == 'S': # check left side
                        count += 1
                if x < len(rows[row]) - 3: # Can have a word to the right+up diagonal
                    if rows[row-1][x+1] == 'M' and rows[row-2][x+2] == 'A' and rows[row-3][x+3] == 'S': # check right side
                        count += 1
                    
            if row < len(rows) - 3:
                if rows[row+1][x] == 'M' and rows[row+2][x] == 'A' and rows[row+3][x] == 'S': # check below
                    count += 1
                if x > 2: # Can have word to left+down diagonal
                    if rows[row+1][x-1] == 'M' and rows[row+2][x-2] == 'A' and rows[row+3][x-3] == 'S': # check left side
                        count += 1
                if x < len(rows[row]) - 3: # Can have a word to the right+down diagonal
                    if rows[row+1][x+1] == 'M' and rows[row+2][x+2] == 'A' and rows[row+3][x+3] == 'S': # check right side
                        count += 1                       
    return count



def x_search(rows):
    count = 0
    for row in range(1, len(rows) - 1):
        a_indices = list(find_all(rows[row], 'A'))
        for a in a_indices:
            if a > 0 and a < len(rows[row])-1: # not in first or last column
                if (rows[row-1][a-1] == 'S' and rows[row+1][a+1] == 'M') or (rows[row-1][a-1] == 'M' and rows[row+1][a+1] == 'S'): # Check \
                    if (rows[row+1][a-1] == 'S' and rows[row-1][a+1] == 'M') or (rows[row+1][a-1] == 'M' and rows[row-1][a+1] == 'S'): #Check /
                        #print(row, a)
                        count += 1
                 
    return count


def find_all(str, substr):
    cur = 0
    while True:
        cur = str.find(substr, cur)
        if cur == -1: return
        yield cur

        cur += len(substr)