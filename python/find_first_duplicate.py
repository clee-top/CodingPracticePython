# Below is from: https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q
# Apparently a Google coding question.
# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for
# which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers,
# return the number for which the second occurrence has a smaller index than the second occurrence of
# the other number does. If there are no such elements, return -1.
#
# Example
#
# For a = [2, 1, 3, 5, 3, 2], the output should be
# firstDuplicate(a) = 3.
#
# There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index
# than the second occurrence of 2 does, so the answer is 3.
#
# For a = [2, 4, 3, 5, 1], the output should be
# firstDuplicate(a) = -1.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer a
#
# Guaranteed constraints:
# 1 ≤ a.length ≤ 105,
# 1 ≤ a[i] ≤ a.length.
#
# [output] integer
#
# The element in a that occurs in the array more than once and has the minimal index for its second occurrence.
# If there are no such elements, return -1.

# Notes: First thing I tried was doing this with lists since the incoming thing is a list. This is too slow because
# lists are 0(n) search/membership in Python. Tried with Dicts, worked.
# Sets are even more elegant because it forces uniqueness.
# We don't really care about the index since the first dupe we find will be the earliest second occurrence.

def first_duplicate(a):

    # Strategy: Search the incoming list and use a temp set to see if you hit a dupe. When you do, return it.
    # If you don't find any dupes return -1.

    search_set = set()

    for number_elem in a:

        if number_elem in search_set:
            return number_elem
        else:
            search_set.add(number_elem)

    # If you can't find any dupes, return -1.
    return -1

# Test cases


first_test_case = first_duplicate([2, 1, 3, 5, 3, 2])
print("First test from example: [2, 1, 3, 5, 3, 2], expected output: 3 -> " + str(first_test_case))

second_test_case = first_duplicate([2, 4, 3, 5, 1])
print("Second test from example: [2, 4, 3, 5, 1], expected output: -1 -> " + str(second_test_case))
