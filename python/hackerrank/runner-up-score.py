# From https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Obvious solution is to sort it, get rid of dupes, then find second largest. Here's a guide on that https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
#
# Input Format
# The first line contains . The second line contains an array   of  integers each separated by a space.
#
# Sample Input 0
#
# 5
# 2 3 6 6 5
# Sample Output 0
#
# 5
# Explanation 0
#
# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

# Hackerrank main driver thing. Input is given.
if __name__ == '__main__':
    n = int(input())

    # Get list from input
    listOfNums = map(int, input().split())

    # Get a list with no dupes
    listNoDupes = list(set(listOfNums))

    # Sort the list. Default sort is ascending by value.
    listNoDupes.sort()

    # The sorted list, with no dupes. Second largest is index -2. There's always between 2 and 10 scores so no 0,1 edge cases. Could be just two scores with same score though...
    if len(listNoDupes) == 1:
        print(listNoDupes[0])
    else:
        print(listNoDupes[-2])




