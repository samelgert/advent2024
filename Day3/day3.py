from helper import *


def run():

    with open('input.txt', 'r') as file:
        input_data = file.read()

    test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undon't()do()don't(),,,,,,,,,,,,mul(8,5))"
    sum = scan_for_mul(input_data)

    print('Part 1:', sum)


if __name__ == '__main__':
    run()
