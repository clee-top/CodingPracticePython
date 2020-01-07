# From: https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # First let's get the numbers into an easy to parse string. Get a blank string and a pointer.
    first_num = ""
    first_pointer = l1

    while first_pointer is not None:
        # Get the next number, make it a string so when added you properly construct the number.
        first_num += str(first_pointer.val)
        first_pointer = first_pointer.next

    second_num = ""
    second_pointer = l2

    while second_pointer is not None:
        # Get the next number, make it a string so when added you properly construct the number.
        second_num += str(second_pointer.val)
        second_pointer = second_pointer.next

    # Reverse them now. Using slicing!
    first_num = first_num[::-1]
    second_num = second_num[::-1]

    # Debugging
    print("First number string is: " + first_num)
    print("Second number string is: " + second_num)

    # Now you have the strings of both numbers. Add them as ints, chop it into a string, construct a new linked list.
    final_num = str(int(first_num) + int(second_num))
    print("Final number is: " + final_num)

    # Make the tail node of newly returned list. Our final number is already the reverse order of the final product
    # So we can just count from 0 - length-1
    # Then construct the rest in a loop so we can get the order right.
    new_node = ListNode(int(final_num[0]))
    new_node.next = None
    previous_node = new_node

    print("Tail node value is: " + str(new_node.val))

    list_pointer = 1
    while list_pointer < len(final_num):
        # Set the new value
        new_node = ListNode(int(final_num[list_pointer]))
        print("Value of next node is: " + str(new_node.val))

        # Set the next of the current node to the previous node.
        new_node.next = previous_node

        # The new previous node is now the current node.
        previous_node = new_node

        # Increment the list pointer to keep it going.
        list_pointer += 1

    return new_node


# Test data making and printing the test lists from the problem to debug.

example_1_first_digit = ListNode(2)
example_1_second_digit = ListNode(4)
example_1_third_digit = ListNode(3)
example_1_first_digit.next = example_1_second_digit
example_1_second_digit.next = example_1_third_digit

example_2_first_digit = ListNode(5)
example_2_second_digit = ListNode(6)
example_2_third_digit = ListNode(4)
example_2_first_digit.next = example_2_second_digit
example_2_second_digit.next = example_2_third_digit

addTwoNumbers(example_1_first_digit, example_2_first_digit)

example_3_first_digit = ListNode(0)

example_4_first_digit = ListNode(0)

addTwoNumbers(example_3_first_digit, example_4_first_digit)

# print(example_1_first_digit.val)
# print(example_1_first_digit.next.val)
# print(example_1_first_digit.next.next.val)
#
# print(example_2_first_digit.val)
# print(example_2_first_digit.next.val)
# print(example_2_first_digit.next.next.val)
