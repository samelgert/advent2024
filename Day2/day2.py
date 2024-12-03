from helper import *


# Not pretty but gets it done

def run():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        input_file = file.read()


    reports = parse_input(input_file)
    
    safe_count = get_safe_count(reports)

    print("Safe Count:" , safe_count)


if __name__ == '__main__':
    run()
