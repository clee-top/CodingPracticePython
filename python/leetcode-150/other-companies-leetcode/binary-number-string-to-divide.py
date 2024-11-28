# You are given a string S of length N which encodes a non-negative number V in a binary form.
# Two types of operations may be performed on it to modify its value these operations are performed until the value of V becomes 0 .
# For example, if string S = "011100", its value V initially is 28. The value of V would change as follows:
# V = 28, which is even: divide by 2 to obtain 14;
# V = 14, which is even: divide by 2 to obtain 7.
# V = 7, which is odd: subtract 1 to obtain 6;
# V = 6, which is even: divide by 2 to obtain 3; •
# V = 3, which is odd: subtract 1 to obtain 2:
# V = 2, which is even: divide by 2 to obtain 1: •
# V = 1, which is odd: subtract 1 to obtain 0.
# Seven operations were required to reduce the value of V to O.

# Write a function: int solution(string &S); that, given a string S consisting of N characters containing a binary representation of the initial value V,
# returns the number of operations after which its value will become o.
# Examples:
# 1. Given S = "011100", the function should return 7. String S represents the number 28, which becomes 0 after seven operations, as explained above.
# 2. Given S = "111", the function should return 5. String encodes the number V
#  Its value will change over the following five operations:
# • V = 7, which is odd: subtract 1 to obtain 6;
# • V = 6, which is even: divide by 2 to obtain 3.
# V = 3, which is odd: subtract 1 to obtain 2,
# V = 2, which is even: divide by 2 to obtain 1; •
# V = 1, which is odd: subtract 1 to obtain 0.
# 3. Given S = "1111010101111', the function should return 22.
# 4. Given string S consisting of "1" repeated 400,000 times, the function should return 799,999.
# Write an efficient algorithm for the following assumptions:
#     • string S consists only of the characters 'O' and/or '1' •
# N, which is the length of string S, is an integer within the range [1..1,000,000):
# the binary representation is big-endian, i.e. the first character of string corresponds to the most significant bit; •
# the binary representation may contain leading zeros.

# Solution = https://stackoverflow.com/questions/59511882/find-the-number-of-steps-a-string-can-be-reduced-to-0

def solution(binary_number_as_string):

    # Simple case, it's already zero.
    if binary_number_as_string == "0":
        return 0

    # print("Pre-Slice binary number: " + binary_number_as_string)
    # Slice the leading zeroes off of it.
    binary_number_as_string = int(binary_number_as_string,2)
    binary_number_as_string = str(bin(binary_number_as_string)[2:])
    # print("Post-Slice binary number: " + binary_number_as_string)

    # Count the ones. Because each one in the binary number takes one operation (I.E slice it to divide by two)
    # Whereas the rest is a function how many numbers total there are to subtract stuff (I.E length of the strength minus the number of ones to get the zeroes, minus 1 to get to zero).
    ones_count = 0
    for current_number in binary_number_as_string:
        if current_number == "1":
            ones_count += 1

    # print("My input was " + str(binary_number_as_string) + " and my ones_count is: " + str(ones_count))

    return_value = ones_count * 2 + (len(binary_number_as_string) - ones_count - 1)

    # print("My answer will be something like: " + str(return_value) )

    return return_value


solution("011100")

testcases = [
    {"name": "test1", "input": "0", "expected": 0},
    {"name": "test2", "input": "011100", "expected": 7},
    {"name": "test3", "input": "111", "expected": 5},
    {"name": "test4", "input": "1111010101111", "expected": 22},
]

for current_case in testcases:
    current_case_result = solution(current_case["input"])
    assert current_case_result == current_case["expected"], f"{current_case['name']} failed, actual = {current_case_result}, expected = {current_case['expected']}"





