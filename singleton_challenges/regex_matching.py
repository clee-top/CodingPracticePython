
12412122222# This function takes a topic described below in the problem set and a topic pattern. It will return true
# if it matches the topic pattern. False if not.


def regex_matching(topic, topicPattern):

    topic_tokenized = topic.split("/")
    pattern_tokenized = topicPattern.split("/")

    # Get the length of the pattern, because we need to know if we're ever at the end of the pattern string.
    pattern_length = len(pattern_tokenized)

    # Counter for checking when we are at the end of the list.
    counter = 1

    # Looping through the incoming topic, make sure each element matches exactly or has the corresponding
    # wildcard
    for topicToken, patternToken in zip(topic_tokenized, pattern_tokenized):

        # print("The topic token is: " + topicToken)
        # print("The pattern token is: " + patternToken)

        # If they're not equal. 1.
        if topicToken != patternToken:

            # 2. Check if plus, and not last entry.
            if patternToken == "+" and counter != pattern_length:
                continue

            # print("The current counter and length of pattern are: " + str(counter) + " " + str(pattern_length))

            # 3. Check # case.
            if patternToken == "#" and counter == pattern_length:
                return True

            # print("Returning false in the wildcard checks.")
            return False

        counter += 1

    return True


# Test cases, both from description.
firstCase = regex_matching("offices/435/meetings/876/people/laura", "offices/+/meetings/+/people/laura")
secondCase = regex_matching("offices/877/meetings/876/people/laura", "offices/877/meetings/#")
print("This first case should return true: " + str(firstCase))
print("This second case should return true: " + str(secondCase))

# Checks:
# 1. Exactly equal is fine. 2. Plus is fine, but not if it's the last entry. 3. # is fine, but only once and as the
# last entry.

# Below is the definition given by prospective employer(Cruise) Above is solution worked out.
#
#
# # MQTT is a simple messaging protocol where producers publish data to a topic and
# subscribers receive that data if they listen to a matching topic pattern.
#
# #●  topics are simple path strings:
# #  ○  offices/435/meetings/876/people/laura
# #●  topic patterns are path strings which can contain two wildcards + (any value) and # (any rest of path)
# #   ○  A subscriber for Laura’s events in any office or meeting:
# #   offices/+/meetings/+/people/laura
# #   ○  A subscriber for all office 877 meeting data:
# #   offices/877/meetings/#
# #   ○  Note + may appear multiple times, but # only once and must be last
#
# Given a topic and topic pattern write a function returning true if they match and false if not.
