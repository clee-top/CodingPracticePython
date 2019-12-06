def first_not_repeating_character(s):

    # Strategy go through every character and add them to a dictionary. Key is char and value is the index.
    # If you encounter it again, remove from dictionary and add it to a "ignore" set to skip further occurences.
    # Once done, sort the dictionary by index and print the min, or if empty return "_"
    #
    # You could probably remove the set and just put the index at -1 or something and skip that to save a bit of space.

    search_dict = {}
    ignore_set = set()

    for string_counter in range(len(s)):

        # Check to see if we need to ignore the char cause it already had a repeat.
        if s[string_counter] not in ignore_set:

            # Check to see if it is a repeat, if so gotta remove it from search space and add to ignore set.
            if s[string_counter] in search_dict:
                del search_dict[s[string_counter]]
                ignore_set.add(s[string_counter])
            else:
                # If it's not previously ignored or a repeat, it's new. Add it to the search space.
                search_dict[s[string_counter]] = string_counter

    # print("The min index is: " + str(the_answer) + " the character at that index is: " + s[the_answer] )
    # print("The list of not repeats are: " + str(search_dict))

    # Dictionaries equivocate to false if empty.
    if search_dict:
        return s[min(search_dict.values())]
    else:
        return "_"


firstTestCase = first_not_repeating_character("abacabad")
print ("The first test case tests \"abacabad\" and expected output is: 'c' -> " + firstTestCase)

secondTestCase = first_not_repeating_character("abacabaabacaba")
print ("The first test case tests \"abacabaabacaba\" and expected output is: '_' -> " + secondTestCase)


# From here: https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC
# Apparently a question Amazon asks.
# Note: Write a solution that only iterates over the string once and uses O(1) additional memory,
# since this is what you would be asked to do during a real interview.
#
# Given a string s, find and return the first instance of a non-repeating character in it.
# If there is no such character, return '_'.
#
# Example
#
# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.
#
# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
#
# For s = "abacabaabacaba", the output should be
# firstNotRepeatingCharacter(s) = '_'.
#
# There are no characters in this string that do not repeat.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string s
#
# A string that contains only lowercase English letters.
#
# Guaranteed constraints:
# 1 ≤ s.length ≤ 105.
#
# [output] char
#
# The first non-repeating character in s, or '_' if there are no characters that do not repeat.