from helper import *



# PROBLEM 1 Prompt:
# Pair up the numbers and measure how far apart they are. 
# Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. 
# For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

# PROBLEM 2 Prompt:
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list. 


def run():

    # Parse the input data
    with open('input.txt', 'r') as file:
        input_file = file.read()
    arr1, arr2 = parse_input_file(input_file)

    
    # PROBLEM 1
    merge_sort(arr1) # Custom merge sort function to practice my sorting algorithms instead of built in sort()
    merge_sort(arr2)
    #arr2 = quick_sort(arr2) # Future work if I have the time
    tot_distance = distance_between(arr1, arr2)
    print("Total distance: ", tot_distance)

    # PROBLEM 2
    score = similarity_score(arr1, arr2)
    print("Similarity Score: ", score)

if __name__ == '__main__':
    run()