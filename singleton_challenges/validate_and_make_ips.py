# Aktana and Flexport asked this question
# IPv4 Address Validator
#
# 127.0.0.1 -> true
#
# 256.256.256.256 -> false


# This function takes an input and returns True if it is a valid. IPv4 Address, False if not.
def validate_ip(number_to_check):

    # Split on the dots since IPv4 addresses have a required format we can which easily this way.
    numbers_split = number_to_check.split(".")

    # Check right # of inputs
    if len(numbers_split) != 4:
        print("Sadly " + number_to_check + " is not an IPv4 address because it is not four numbers split with dots.")
        return False

    for possible_number in numbers_split:

        # Check if # and all are in right range.
        if int(possible_number[0]) == 0 and len(possible_number) > 1:
            # print("Sadly, " + number_to_check + " is a not an IPv4 address because one of its components has a leading 0 digit.")
            return False

        # Make sure the component is a number.
        if possible_number.isdigit() == False:
            # print("Sadly, " + number_to_check + " is a not an IPv4 address because one of its components it is not a number.")
            return False

        # Make sure the component is between 0 and 255 for level IP address.
        if int(possible_number) > 255 or int(possible_number) < 0:
            # print("Sadly " + number_to_check + " is not an IPv4 address because one of its components is not between 0 and 255.")
            return False

    # print("Found a valid ip at: " + str(number_to_check))
    return True

# Test cases, correct and edge cases.
# validate_ip("256.256.256.256")
# validate_ip("127.0.0.1")

# validate_ip("127.0.0.a")
# validate_ip("0127.0.0.1")


# IPv4 Address Maker
# Given a well formatted string, attempt to determine if you can make it a valid IP address by adding
# three dots in places that would make it a valid IP address.
# N -> This is another a geeks for geeks problem (Sigh) https://www.geeksforgeeks.org/program-generate-possible-valid-ip-addresses-given-string/
def ip_maker(input_number):

    input_length = len(input_number)

    # Check string isn't too long. IPV4 can'th ave more then 12 numbers.
    if input_length > 12:
        return []

    # Var to hold the strings we're constructing and return list of valid combos.
    new_string = input_number
    return_list = []

    # Generating different combinations.
    for first_dot in range(1, input_length - 2):
        for second_dot in range(first_dot + 1, input_length - 1):
            for third_dot in range(second_dot + 1, input_length):

                new_string = new_string[:third_dot] + "." + new_string[third_dot:]
                # print("third_dot is: " + str(third_dot) + " new string looks like this: " + new_string)

                new_string = new_string[:second_dot] + "." + new_string[second_dot:]
                # print("second_dot is: " + str(second_dot) + " new string looks like this: " + new_string)

                new_string = new_string[:first_dot] + "." + new_string[first_dot:]
                # print("first_dot is: " + str(first_dot) + " new string looks like this: " + new_string)

                # Check for the validity of combination
                if validate_ip(new_string):
                    return_list.append(new_string)
                new_string = input_number

    print("Return list of valid IP's looks like this: " + str(return_list))
    return return_list

# ip_maker("00001")
ip_maker("25525511135")
