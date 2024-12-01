
def parse_input_file(input_file):
    arr1 = []
    arr2 = []
    lines = input_file.splitlines()
    for line in lines:
        nums = line.split("  ")
        arr1.append(int(nums[0]))
        arr2.append(int(nums[1]))
    
    return arr1, arr2


def merge_two_sorted_lists(a, b, merged):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            merged[k] = a[i]
            i += 1
        else:
            merged[k] = b[j]
            j += 1
        k += 1

    # Merge remaining elements from the longer array
    while i < len_a:
        merged[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        merged[k] = b[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)


# Sums the total difference between each element at the same index in two arrays
def distance_between(arr1, arr2):
    i = 0
    distance = 0
    if len(arr1) != len(arr2):
        print("Lists have different lengths")
        return -1
    
    for i in range(len(arr1)):
        distance += abs(arr1[i] - arr2[i])
    
    return distance


def similarity_score(arr1, arr2):
    location_dict = occurence_dictionary(arr2)
    score = 0

    for num in arr1:
        if num in location_dict:
            score += (num * location_dict[num])
    
    return score

# Returns the number of times each value appears in its array in the form of a dictionary
def occurence_dictionary(arr):
    dict = {}

    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    
    return dict