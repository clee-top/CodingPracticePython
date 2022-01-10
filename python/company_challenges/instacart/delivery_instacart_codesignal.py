# -> Code Signal company branded test, this solution passed all tests + hidden test cases.

# Instacart customers are able to set the solution window during which they want to receive their groceries.
# There are always plenty of shoppers in the area ready to take a customer's order, but unfortunately they can't always do it right away.
# Before taking an order a shopper wants to ensure they will make it in time. They also don't want to stay idle, so arriving early isn't an option either.
#
# Our task is to implement an algorithm that determines whether shoppers should take the given order or not.
#
# For each shopper you know their travel speed, distance to the store and the estimated amount of time they will spend there.
# Figure out which of them can take the order, assuming it is known when the customer wants to receive the groceries and the distance between their house and the store.
#
# Example
#
# For order = [200, 20, 15] and shoppers = [[300, 40, 5], [600, 40, 10]], the output should be
#
# solution(order, shoppers) = [false, true].
#
# The store is located 200 m away from the customer's house.
#
# The customer will be ready to receive the groceries in 20 minutes, but they shouldn't be delivered more than 15 minutes late.
#
# The first shopper is 300 m away from the store, his speed is 40 m/min, and he will spend 5 minutes in the store, which means that he will need (300 + 200) / 40 + 5 = 17.5 minutes to fulfill the
# order. This will leave him with 20 - 17.5 = 2.5 idle minutes, so he shouldn't take the order.
#
# The second shopper is 600 m away from the store, his speed is 40 m/min, and he will spend 10 minutes in the store, which means it will take him (600 + 200) / 40 + 10 = 30 minutes to fulfill the
# order. The customer can wait for 20 + 15 = 35 minutes, which means that the shopper will make it in time.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer order
#
# The order is given as an array of 3 positive integers.
# order[0] is the distance from the customer's home to the store in meters,
# order[1] is the time by which the customer will be ready to receive the delivery in minutes,
# and order[2] is the number of minutes they are willing to wait.
#
# Guaranteed constraints:
# order.length = 3,
# 1 ≤ order[i] ≤ 1000.
#
# [input] array.array.integer shoppers
#
# Each element of this array represents a shopper. For each shopper three positive integers are stored in the exact given order:
# their distance from the shop in meters, their speed in meters per minute and the estimated time they will spend in the store in minutes.
#
# Guaranteed constraints:
# 1 ≤ shoppers.length ≤ 5,
# shoppers[i].length = 3,
# 1 ≤ shoppers[i][j] ≤ 1000.
#
# [output] array.boolean
#
# For each shopper return if they should take the order or not.


def solution(order, shoppers):

    # Start with initial variables. We know we need a list of Booleans to eventually return we are filling with answers.
    return_list = []

    # Iterate through every shopper in the list and see if they should take the order. Append answer to return list.
    for shopper in shoppers:
        return_list.append(will_take_order(order,shopper))

    return return_list


# Helper function. Toss it an order and a shopper and it will pass back True/False if they should take the order or not.
# an easy abstraction to make, though it's simple enough to go in the funciton above.
def will_take_order(incoming_order,incoming_shopper):

    # Calculate total time needed for shopper
    distance_from_shopper_to_store = incoming_shopper[0]
    shopper_speed = incoming_shopper[1]
    time_to_shop_in_store = incoming_shopper[2]
    distance_from_customer_to_store = incoming_order[0]
    total_distance_traveled_for_shopper = distance_from_shopper_to_store + distance_from_customer_to_store

    # Worked out total shop time formula. Ceiling the possible float to round conservatively up to the nearest minute since
    # flooring it might give a false positive we should probably avoid. And the preferences for shoppers are whole integers.
    # N -> Hidden test case in Code Signal failed which worked when I didn't ceiling the values, I assume because of a fucky test case that doesn't take into the account of ceiling this value.
    # total_time_shopping = math.ceil((total_distance_traveled_for_shopper/shopper_speed) + time_to_shop_in_store)
    total_time_shopping = (total_distance_traveled_for_shopper/shopper_speed) + time_to_shop_in_store

    # Calculate minumum and total wait time for customer which are the conditionals we're working off of.
    customer_minimum_expected_time = incoming_order[1]
    customer_willing_to_wait_time = incoming_order[2]
    customer_max_wait_time = customer_minimum_expected_time + customer_willing_to_wait_time

    # Boil that down into this conditional. Total time has to be above minumum and below maximum wait itme.
    if (total_time_shopping >= customer_minimum_expected_time) and (total_time_shopping <= customer_max_wait_time):
        return True
    else:
        return False
