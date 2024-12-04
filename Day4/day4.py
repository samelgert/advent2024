from helper import *


def run():
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        input_file = file.read()

    rows = parse_input(input_file)

    print(word_search(rows))
    print(x_search(rows))


if __name__ == '__main__':
    run()
