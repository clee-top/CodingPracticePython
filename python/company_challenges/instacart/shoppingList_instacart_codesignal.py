# As part of an Instacart beta testing group, Sara is trying out a brand new feature that automatically estimates the combined cost of the items in her handwritten shopping list. Her list contains
# both items and their prices. All Sara has to do is snap a photo of her list with the Instacart app, and she gets a quick estimate of what everything will cost.
#
# Sara asked for your help, so it is up to you to devise an algorithm that calculates the cost after the image is converted into plain text. All you need to do is extract all numbers from the given
# string items and sum them up.
#
# Example
#
# For items = "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4", the output should be
# solution(items) = 7.48;
# For items = "blue suit for 24$, cape for 12.99$ & glasses for 15.70", the output should be
# solution(items) = 52.69.
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string items
#
# A shopping list given as a string. It is guaranteed that the only numbers in it are dollar prices for different items. Note that although each price is given in dollars, you do not know their
# exact form. Each of them can either be an integer, or a decimal number with one or two decimal places and it may or may not be followed by a dollar sign. However, you may assume that if there is
# a period ('.') between two digits, then it's a decimal mark.
#
# Guaranteed constraints:
# 0 ≤ items.length ≤ 6 · 104.
#
# [output] float
#
# The total cost of all items.

# Need regular expression split
import re


def solution(items):
    # Notes: Input looks like it's a big string of list entries split by ";" and then ",". Split those, then add any numbers you
    # find in a list
    item_list = []
    # Saved and created this here- > https://regex101.com/r/elWDra/1
    # from here https://stackoverflow.com/questions/31323783/regex-for-prices-with-euros-pounds-and-dollars
    item_list = re.findall(r"\d+\.?\d{0,2}", items)
    # Keep a running total we eventually have to return.
    running_total = 0

    # Now I have a list of items. I can iterate through them and keep a running total. The above may have been a not-needed
    # step since I probably could've just been looking for numbers? We'll see.
    for item in item_list:
        running_total += float(item)

    # Test code for Code Signal to see what's coming out.
    # return(str(item_list))
    return running_total
