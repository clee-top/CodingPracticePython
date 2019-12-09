"""
Coding practice - Use any preferred programing language

Validate an IP address (IPv4). An address is valid if and only if it is in the form "X.X.X.X", where each X is a number from 0 to 255.

For example, "12.34.5.6", "0.23.25.0", and "255.255.255.255" are valid IP addresses, while "12.34.56.oops", "1.2.3.4.5", and "123.235.153.425" are invalid IP addresses.
"""


# N: I fudged up and put in brackets, parentheses and semi-colons at first.
# That'll teach me to practice Java right before trying to use Python.
# I'm going to add print statements for debugging.

# Input one possible ip address. Return true if valid ip, false if not.
def check_valid_ip(input_ip):
    # Validate the input has the right format of 4 numbers separated by dots.
    number_split = input_ip.split(".")

    # Make sure that the input is a number/digit.
    for possible_number in number_split:
        # N: Apparently you can simplify this to: not possible_number.isDigit(). Harder to read for a laymen I think?
        # N: Further not, you incorrectly had "isDigit" instead of the correct "isdigit" function name.
        if possible_number.isdigit() == False:
            print("Found a bad IP! And it's " + input_ip)
            return False

    if len(number_split) != 4:
        # Not the right number between dots, so return False.
        print("Found a bad IP! And it's " + input_ip)
        return False
    else:
        # Check each number is in the right range.
        for number in number_split:
            # N: I fucked up with wrote a big "OR" here. Not sure why.
            if int(number) > 255 or int(number) < 0:
                print("Found a bad IP! And it's " + input_ip)
                return False

    # If all checks pass, return True.
    print("Found a valid IP! And it's " + input_ip)
    return True


# N: I only had one test bef
check_valid_ip("12.34.5.6")
# N: I only had one test from the description before proctor asked me to stop. Hopefully a good sign?
# Adding the rest from the description simply because I feel like it'd be nicer that way.
check_valid_ip("0.23.25.0")
check_valid_ip("255.255.255.255")
check_valid_ip("12.34.56.oops")
check_valid_ip("1.2.3.4.5")
check_valid_ip("123.235.153.425")
