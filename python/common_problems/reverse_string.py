# Reverse a string without slicing. This is asked. ALOT by everyone. This solution doesn't use reverse or slicing so people don't call it cheating.

def reverse_string(input_string):
    new_string = ""

    # Tricky -> Strings are zero indexed, so you need to start at the index -l of the length for the start of range.
    # Tricky -> Range goes to whole number BEFORE you stop. So to stop at 0 the second parameter needs to be -1 (The next -1 step from 0))
    for index in range(len(input_string) - 1, -1, -1):
        # print("Element is: " + str(index))
        # Append to a new string to shove it in a variable.
        print(input_string[index])

    return new_string


reverse_string("Meow")
