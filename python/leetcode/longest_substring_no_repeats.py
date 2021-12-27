# From leetcode

# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s: str) -> int:

    # Get the length
    input_length = len(s)

    # Starting point of current substring.
    current_sub_index = 0

    # Maximum length substring without repeating characters.
    longest_substring = 0

    # Starting index of maximum length substring.
    max_start_index = 0

    # Hash Map to store last occurrence of each already visited character.
    last_seen_map = {}

    # Pre-populate: The "first" last occurrence of first character is index 0
    last_seen_map[s[0]] = 0

    # Loop through the string.
    for index in range(1, input_length):

        # If this character is not present in hash, then this is first occurrence of this character, store this in hash.
        if s[index] not in last_seen_map:
            last_seen_map[s[index]] = index

        else:
            # If this character is present in hash then this character has previous occurrence, check if that occurrence is before or after starting point of current substring.
            if last_seen_map[s[index]] >= current_sub_index:

                # Find length of current substring and update substring max length and start accordingly.
                current_sub_length = index - current_sub_index

                if longest_substring < current_sub_length:
                    longest_substring = current_sub_length
                    max_start_index = current_sub_index

                # Next substring will start after the last occurrence of current character to avoid its repetition.
                current_sub_index = last_seen_map[s[index]] + 1

            # Update last occurrence of current character.
            last_seen_map[s[index]] = index

            # Compare length of last substring with maxlen and update maxlen and start accordingly.
            if longest_substring < index - current_sub_index:
                longest_substring = index - current_sub_index
                max_start_index = current_sub_index

    # The required longest substring without repeating characters is from string[start] to string[start+maxlen-1].
    print("Longest substring is: " + s[max_start_index: max_start_index + longest_substring])
    return len(s[max_start_index: max_start_index + longest_substring])


lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("bbbbb")

