# From Geeks for geeks-> https://www.geeksforgeeks.org/lexicographically-largest-string-by-merging-identical-adjacent-letters-e-g-aa-into-the-next-letter/
# Given a positive integer N representing a string of length N with only the letter ‘z,’ the task is to find the
# Lexicographically largest string by merging adjacent identical letters into a single letters of previous alphabet
# (e.g. Merging “zz” would become “y” and Merging “yy” would become “x” and so on).


# Function to construct a string based on the powers of 2 in the given number 'n'
def construct_string(number_of_iterations):
    # Need these to construct a new string.
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"

    # Keep track of current return string, starts empty.
    return_string = ""

    # Continue the loop until 'number of iterations' becomes zero
    while number_of_iterations:
        # Find the position and power of 2 for 'n'
        position, current_value = largest_power_of_two(number_of_iterations)
        # Add the corresponding character to the result string
        return_string += alphabet_string[position]
        # Subtract the value corresponding to the character added
        number_of_iterations -= current_value
    return return_string  # Return the constructed string


# Function to find the largest power of 2 in a given number an integer.
def largest_power_of_two(input_number):
    # Initialize return value.
    largest_power_to_return = 0

    # Loop through bit positions from 30 to 0 (inclusive) to find the highest bit that is set to 1.
    for i in range(30, -1, -1):
        # Check if the bit is set (equals 1)
        if (1 << i) & input_number:
            # Store the position of the highest bit that is set
            largest_power_to_return = i
            # Exit the loop after finding the highest bit
            break
    # Limit the position to 25 as 'z' (2^25) is the lowest character needed
    largest_power_to_return = min(25, largest_power_to_return)
    # Return the position and the corresponding power of 2
    return largest_power_to_return, 1 << largest_power_to_return


# Main function to demonstrate the code
def main():
    n = 67108876
    # n = 10
    result = construct_string(n)  # Call the function to construct the string
    print(result)  # Print the final constructed string


# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Execute the main function

