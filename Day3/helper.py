

def scan_for_mul(mul_str):
    sum = 0
    enabled = True


    while mul_str.find('mul(') != -1:
        do_index = mul_str.find('do()')
        dont_index = mul_str.find("don't()")
        index = mul_str.find('mul(')

        # If mul is the next instruction
        if (index < do_index or do_index == -1) and (index < dont_index or dont_index == -1):
            i = 4 # Goes to end of 'mul('
            if enabled:
                num1 = ''
                num2 = ''
                if mul_str[index + i].isnumeric():

                    while mul_str[index + i].isnumeric():
                        num1 += mul_str[index + i]
                        i += 1
                    

                    if mul_str[index + i] == ',':
                        i += 1
                        #check second num
                        while mul_str[index + i].isnumeric():
                            num2 += mul_str[index + i]
                            i += 1

                        if mul_str[index + i] == ')':
                            sum += (int(num1) * int(num2))

            mul_str = mul_str[index + i: ] # Cut off beginning of string

        else:
            if (dont_index < do_index or do_index == -1) and dont_index != -1:
                enabled = False
                mul_str = mul_str[dont_index + 6:]
            elif (do_index < dont_index or dont_index == -1) and do_index != -1:
                enabled = True
                mul_str = mul_str[do_index + 3:]
        
            

        
    
    return sum