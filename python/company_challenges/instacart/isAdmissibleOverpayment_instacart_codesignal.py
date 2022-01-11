# After recently joining Instacart's beta testing developer group, you decide to experiment with their new API. You know that the API returns item-specific display-ready strings like 10.0% higher
# than in-store or 5.0% lower than in-store that inform users when the price of an item is different from the one in-store. But you want to extend this functionality by giving people a better sense
# of how much more they will be paying for their entire shopping cart.
#
# Your app lets a user decide the total amount x they are willing to pay via Instacart over in-store prices. This you call their price sensitivity.
#
# Your job is to determine whether a given customer will be willing to pay for the given items in their cart based on their stated price sensitivity x.
#
# Example
#
# For
# prices = [110, 95, 70],
#
# notes = ["10.0% higher than in-store",
#          "5.0% lower than in-store",
#          "Same as in-store"]
# and x = 5, the output should be
# solution(prices, notes, x) = true.
#
# In-store prices of the first and the second items are 100, and the price of the third item is 70, which means the customer is overpaying 10 - 5 + 0 = 5, which they are willing to do based on
# their price sensitivity.
#
# For
# prices = [48, 165],
#
# notes = ["20.00% lower than in-store",
#          "10.00% higher than in-store"]
# and x = 2, the output should be
# solution(prices, notes, x) = false.
#
# The in-store price of the first item is 60, and the second item is 150. The overpayment equals 15 - 12 = 3, which is too much for the customer to be willing to pay.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.float prices
#
# Positive numbers, representing prices of the items in the shopping cart.
#
# Guaranteed constraints:
# 1 ≤ prices.length ≤ 10,
# 20.0 ≤ prices[i] ≤ 35.0 · 103.
#
# [input] array.string notes
#
# Array of the same length as prices. For each valid i notes[i] has one of the following forms:
#
# "x% higher than in-store", which means that Instacart price of the ith item is x% higher than the local one;
# "x% lower than in-store", which means that Instacart price of the ith item is x% lower than the local one;
# "Same as in-store", which means that the ith item costs the same in Instacart and in the local store,
# where x is a positive float number with the decimal point and at least one digit after it.
#
# Guaranteed constraints:
# notes.length = prices.length,
# 16 ≤ notes[i].length ≤ 30.
#
# [input] float x
#
# A non-negative float, the maximum amount of money the customer is willing to overpay.
#
# Guaranteed constraints:
# 0 ≤ x ≤ 150.0.
#
# [output] boolean
#
# true if the overpayment is admissible, false otherwise.

import math


def solution(prices, notes, x):
    running_difference = 0

    # Make a function that goes through the prices and notes and returns running overcharge.
    for index in range(0, len(prices)):
        running_difference += check_price(prices[index], notes[index])
        print("The running difference is: {}.".format(running_difference))

    # First check if they're really close. If they are just return true, since all the tests are picky about that. Floats suck.
    if math.isclose(running_difference, x):
        return True
    # If it's just plain larger, false. Else. We're good.
    elif running_difference > x:
        return False
    else:
        return True


def check_price(price, note):

    # Split on spaces. They were very nice on our inputs.
    split_string = note.split(" ")

    # Main paths. No price difference, or some price difference up or down.
    if split_string[0] == "Same":
        # If it's the same there is no difference, and we don't care, so just return 0.
        return 0
    # If it's higher we get the percent raw and times it by .01 to get a raw float percentage.
    elif "higher" in split_string[1]:
        percent_difference = float(split_string[0].strip("%")) * .01
    # If it's not higher it's lower. Literally only other input it can have. Times it by -1 so in later generic formula works
    else:
        percent_difference = float(split_string[0].strip("%")) * .01 * -1

    actual_price = price / (1 + percent_difference)

    # Now we have the modified price and the actual price. Now all we want is the difference.
    return price - actual_price

    # print("The percent difference is {}. OG price is: {}. The actual price for the items is: {}"
    #      .format(percent_difference,price, actual_price))
