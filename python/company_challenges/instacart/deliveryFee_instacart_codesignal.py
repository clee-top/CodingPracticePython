# To make sure that groceries can always be delivered, Instacart tries to equally distribute delivery requests throughout the day by including an additional delivery fee during busy periods.
#
# Each day is divided into several intervals that do not overlap and cover the whole day from 00:00 to 23:59. For each i the delivery fee in the intervals[i] equals fees[i].
#
# Given the list of delivery requests deliveries, your task is to check whether the delivery fee is directly correlated to the order volume in each interval i.e. the interval_fee /
# interval_deliveries value is constant for each interval throughout the day.
#
# Example
#
# For
# intervals = [0, 10, 22], fees = [1, 3, 1], and
#
# deliveries = [[8, 15],
#               [12, 21],
#               [15, 48],
#               [20, 17],
#               [23, 43]]
# the output should be
# solution(intervals, fees, deliveries) = true.
#
# The day is divided into 3 intervals:
#
# from 00:00 to 09:59, the first delivery was made, fees[0] / 1 = 1;
# from 10:00 to 21:59, the 2nd, 3rd and 4th deliveries were made, fees[1] / 3 = 1;
# from 22:00 to 23:59, the last delivery was made, fees[2] / 1 = 1.
# interval_fee / interval_deliveries = 1 for each interval, so the answer is true.
#
# Check out the image below for better understanding:
#
#
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.integer intervals
#
# Each interval starts at xx:00 and ends at yy:59, where xx equals intervals[i] and yy equals intervals[i + 1] - 1, or 23 if intervals[i + 1] doesn't exist. intervals[i] represents the hour at
# which the ith interval starts. It is guaranteed that intervals[0] = 0.
#
# Guaranteed constraints:
# 1 ≤ intervals.length ≤ 24,
# 0 ≤ intervals[i] ≤ 23,
# intervals[0] = 0.
#
# [input] array.integer fees
#
# Array of non-negative integers of the same length as intervals. fees[i] is the delivery fee in the ith interval.
#
# Guaranteed constraints:
# fees.length = intervals.length,
# 0 ≤ fees[i] ≤ 105.
#
# [input] array.array.integer deliveries
#
# Deliveries in the order they were made. Each delivery is represented as the [h, m] array, h is the hour and m is the minute it was done. It is guaranteed that there were no deliveries at the same
# time.
#
# Guaranteed constraints:
# 1 ≤ deliveries.length ≤ 30,
# 0 ≤ deliveries[i][0] ≤ 23,
# 0 ≤ deliveries[i][1] ≤ 59.
#
# [output] boolean
#
# true if the delivery fee is directly correlated to the order volume in each interval, false otherwise.


def solution(intervals, fees, deliveries):
    # Initial delivery fee constant is empty. The first time the helper function is run, it populates and
    # forces a comparison against it against all subsequent runs.
    delivery_fee_constant = None

    # Got a helper function, just need a for loop to go through every interval.
    for index in range(0, len(intervals)):
        # Special case, populate initial delivery fee constant in first run and pass in that it is none.
        # Otherwise, just pass it in
        if index == 0:
            delivery_fee_constant, bool_check = check_interval(intervals, fees, deliveries, index, None)
        else:
            bool_tuple = check_interval(intervals, fees, deliveries, index, delivery_fee_constant)
            bool_check = bool_tuple[1]
        if bool_check == False:
            return False
        # Debug statement
        # print("Interval " + str(index+1) + " is coming back as " + str(bool_check))
    # If it never pops false then presumably all of them were true and we're goodskies.
    return True


def check_interval(intervals, fees, deliveries, interval_index, delivery_fee_constant):
    # Keep running total of deliveries for this interval.
    deliveries_in_interval = 0

    # Special casing for boundaries. Zero index interval has min_bound of zero. Normal case is just index time.
    if interval_index == 0:
        interval_min_bound = 0
    else:
        interval_min_bound = intervals[interval_index] * 100

    # Special casing for last interval_index in which last index is from index time to 24:00.
    # Normal casing is just the next in the interval list.
    if interval_index == (len(intervals) - 1):
        interval_max_bound = 2400
    else:
        interval_max_bound = intervals[interval_index + 1] * 100

    for completed_order in deliveries:
        # Makes an easy to compare integer out of the delivery time.
        deliver_time_as_int = completed_order[0] * 100 + completed_order[1]

        # If it's after the min, and before the max, the delivery took place in this interval, and we should count it.
        # print("Checking entry delivered at {} and we want it greater then {} and less then {}"
        # .format(deliver_time_as_int,interval_min_bound,interval_max_bound))

        if (deliver_time_as_int >= interval_min_bound) and (deliver_time_as_int < interval_max_bound):
            deliveries_in_interval += 1

    # Special casing. What if there are no deliveries? Dividing by zero is bad,
    # but it's also possible that the fees array has zero deliveries in there, so here we go.
    if deliveries_in_interval == 0:
        if fees[interval_index] == 0:
            # Super special casing if our first interval setting the tone has this, the constant to compare becomes 0.
            if delivery_fee_constant is None:
                delivery_fee_constant = 0
            return 0, True
        else:
            return 0, False

    current_fee_delivery_ratio = fees[interval_index] / deliveries_in_interval

    # print("Interval {} has {} total charged fees and {} total deliveries. The delivery fee constant is {}"
    # .format(interval_index+1,fees[interval_index],deliveries_in_interval,delivery_fee_constant))

    # General case. If we don't the constant yet, this is the first interval, and we're making it.
    if delivery_fee_constant is None:
        delivery_fee_constant = current_fee_delivery_ratio
        return delivery_fee_constant, True
    else:
        # Otherwise, we have a constant, and it needs to equal our current distribution to be true.
        if current_fee_delivery_ratio == delivery_fee_constant:
            return 0, True
        else:
            return 0, False
