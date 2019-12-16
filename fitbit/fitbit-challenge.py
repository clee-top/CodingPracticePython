# Legend:
# N -> Notes I put in later.

# Below is description given by proctor
# Please write a function reverse_array() that returns the provided array in reverse order.
#   NOTE: Do not use built-in array reversal functions
# Example:
# >>> a = ['a',2,3,9,5]
# >>> print(reverse_array(a))
# [5,9,3,2,'a']

def reverse_array(input_array):

    # Initialize a new array.
    # N -> Proctor noted it would've been more efficient to reverse in place instead of making a whole new array.
    return_array = []

    # Slice the array, going backwards, should functionally reverse it.
    return_array = input_array[::-1]

    # print("The reversed array kind of looks like this: " + str(return_array))

    return return_array

reverse_array([1,2,3,4,5])

# Below is description given by proctor
# Please write a find_duplicates() function that takes
# in an array and makes a new array with any values that appear
# more than once. The returned array should not have any duplicates.
# Example:
# >>> a = [8, 1, 2, 3, 2, 4, 1, 1, 2]
# >>> print(find_duplicates(a))
# [1, 2]

def find_duplicates(input_array):

    # Make a set, iterate through array, if you find duplicates, add to another array to return.
    # N -> Also could've just used this set and returned it as an array. Less lines that way too.
    duplicate_set = set()

    # Initialize return array.
    return_array = []

    # Iterate through each element
    for element in input_array:
        # If not in set, add it.
        if element not in duplicate_set:
            duplicate_set.add(element)
        else:
            if element not in return_array:
                return_array.append(element)

    # print("The duplicates list looks like this: " + str(return_array))

    return return_array

find_duplicates([8, 1, 2, 3, 2, 4, 1, 1, 2])
