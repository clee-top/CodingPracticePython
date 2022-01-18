# If you have a task that you need to complete on a regular basis, you can set it up in Asana as a recurring task. This allows you to schedule the task to repeat on specific days of the week every
# k weeks.
#
# For instance, you could set up a recurring task that reminds you to call your sister on Tuesday and Friday every 3 weeks. You set up the first instance of the task for Tuesday, March 1. The next
# instance will fall on Friday, March 4. The third instance will fall 3 weeks later on Tuesday, March 22, the fourth instance will fall on Friday, March 25, the fifth instance will fall on Tuesday,
# April 12, and so on.
#
# Given a firstDate that represents the day your recurring task becomes active, an array daysOfTheWeek that indicates which days of the week the task should occur on, and a number k that represents
# the interval between weeks on which the task occurs, return an array that contains the first n dates on which the task is scheduled.
#
# In this task, you'll likely need to know how long the months are and the names of the days of week, provided here:
#
# Month lengths from January to December: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.
# During leap years February has 29 days.
# Names of weekdays: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday".
# January 1, 2015 was a Thursday.
# Example
#
# For firstDate = "01/01/2015", k = 2, daysOfTheWeek = ["Monday", "Thursday"], and n = 4, the output should be
#
# solution(firstDate, k, daysOfTheWeek, n) =
# ["01/01/2015", "05/01/2015", "15/01/2015", "19/01/2015"]
#
#
# firstDate falls on a Thursday. The first Monday after it is January 5, "05/01/2015". Since k = 2, the next two days for which the task is scheduled are Thursday, January 15, and Monday, January 19.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] string firstDate
#
# A string in the format "dd/mm/yyyy", representing a date either in the past or the future.
#
# Guaranteed constraints:
# "01/01/1900" ≤ firstDate ≤ "31/12/3999".
#
# [input] integer k
#
# A positive integer.
#
# Guaranteed constraints:
# 1 ≤ k ≤ 20.
#
# [input] array.string daysOfTheWeek
#
# An array containing from 1 to 7 distinct elements, inclusive, each of which equals a weekday name. Days appear in the same order they are given in the description. It's guaranteed that the day of
# the week on which the firstDate falls is present in this list.
#
# Guaranteed constraints:
# 1 ≤ daysOfTheWeek.length ≤ 7.
#
# [input] integer n
#
# Guaranteed constraints:
# 1 ≤ n ≤ 15.
#
# [output] array.string
#
# An array containing the first n dates (including the first one) on which the task is scheduled, in chronological order.

# For firstDate = "01/01/2015", k = 2, daysOfTheWeek = ["Monday", "Thursday"], and n = 4, the output should be
# solution(firstDate, k, daysOfTheWeek, n) = ["01/01/2015", "05/01/2015", "15/01/2015", "19/01/2015"]

# day, month, years, days_to_add
# add_days_to_a_date(1, 1, 2015, 7)


def solution(firstDate, k, daysOfTheWeek, n):
    # First off we need to build a list of the dates we're passing back.
    dates_to_return = []
    number_of_appointments = n
    weeks_until_recurrence = k

    # That's easy, now we need to iterate. Let's do a loop and prime it with the first date.
    # We can get the ints of the first date by splitting the first date that was passed in.
    # This was our first occurrence and where we are starting
    day_splitter = firstDate.split("/")
    current_day = int(day_splitter[0])
    current_month = int(day_splitter[1])
    current_year = int(day_splitter[2])

    # Using this to keep track of the offset of the last day an appointment was scheduled on that day.
    days_of_week_map = {"Sunday": None, "Monday": None, "Tuesday": None, "Wednesday": None, "Thursday": None, "Friday": None, "Saturday": None}

    # Go through one full week starting at current day.
    for week_index in range(0, 7):

        # Initialize the current day of the week as a string.
        check_day_of_week_string = get_day_of_week_from_date_string(current_day, current_month, current_year)

        # If that day is in the "occurs on" array, then we need to schedule that appointment.
        if check_day_of_week_string in daysOfTheWeek:

            # Base case, we've never scheduled anything on this day yet. So we can presume if we're seeing it we can make an appointment.
            if days_of_week_map[check_day_of_week_string] is None:

                # Set a counter in here to save the date we last scheduled an appointment on this day. We need to check if it's been X * weeks it occurs
                # when it is not none to see if we need to schedule on that day.
                days_of_week_map[check_day_of_week_string] = offset_days_from_start_of_year(current_day, current_month, current_year)

                # Append this date!
                dates_to_return.append("{:02d}/{:02d}/{:02d}".format(current_day, current_month, current_year))
                number_of_appointments -= 1

            elif offset_days_from_start_of_year(current_day, current_month, current_year) - days_of_week_map[check_day_of_week_string] >= (k * 7):

                # Another base case. We encountered a day, and it's been more than x weeks. Add it. Move on.
                days_of_week_map[check_day_of_week_string] = offset_days_from_start_of_year(current_day, current_month, current_year)

                # Append this date!
                dates_to_return.append("{:02d}/{:02d}/{:02d}".format(current_day, current_month, current_year))
                number_of_appointments -= 1

        # Brute force, check one day at a time.meowmeow

        current_day, current_month, current_year = add_days_to_a_date(current_day, current_month, current_year, 1)

    # Go through days of week. Mark the nones and delete them.
    new_recurrence_list = []
    for key in days_of_week_map:
        if days_of_week_map[key] is None:
            delete_list.append(key)

    for delete_target in delete_list:
        del days_of_week_map[delete_target]

    print("Offset of the last day checked is: {} ".format(offset_days_from_start_of_year(current_day, current_month, current_year)))
    print("Days of the week map looks like this {}".format(days_of_week_map))



    # Loop through other weeks now that we have a map we can use.
    # while n > 0:




    print("Current appointment list if: {}".format(dates_to_return))
    return dates_to_return


# Given a year, returns if it is a leap year according to Gregorian calendar leap year rules. https://en.wikipedia.org/wiki/Leap_year
def is_leap_year(year_to_check_for_leap_year):
    if year_to_check_for_leap_year % 100 != 0 and year_to_check_for_leap_year % 4 == 0 or year_to_check_for_leap_year % 400 == 0:
        return True
    else:
        return False


# Given a date, returns number of days elapsed from the beginning of the current year.
def offset_days_from_start_of_year(day_to_check_offset, month_to_check_offset, year_to_check_offset):
    days_offset = day_to_check_offset

    # The following is adding all the days present in the subsequent months in the offset as determined by what months it is
    # and how many days are in that month.
    if month_to_check_offset - 1 == 11:
        days_offset += 335
    if month_to_check_offset - 1 == 10:
        days_offset += 304
    if month_to_check_offset - 1 == 9:
        days_offset += 273
    if month_to_check_offset - 1 == 8:
        days_offset += 243
    if month_to_check_offset - 1 == 7:
        days_offset += 212
    if month_to_check_offset - 1 == 6:
        days_offset += 181
    if month_to_check_offset - 1 == 5:
        days_offset += 151
    if month_to_check_offset - 1 == 4:
        days_offset += 120
    if month_to_check_offset - 1 == 3:
        days_offset += 90
    if month_to_check_offset - 1 == 2:
        days_offset += 59
    if month_to_check_offset - 1 == 1:
        days_offset += 31

    # Need an extra day for leap years if present.
    if is_leap_year(year_to_check_offset) and month_to_check_offset > 2:
        days_offset += 1

    return days_offset


# Given a year and days elapsed in it, finds date by storing results in d and m.
def date_from_offset(days_offset, year_of_date):
    # Array to store off offsets of days in each month. Similar to above function.
    month_offset_array = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year_of_date):
        month_offset_array[2] = 29

    for month_index in range(1, 13):
        if days_offset <= month_offset_array[month_index]:
            break
        days_offset = days_offset - month_offset_array[month_index]

    # Making it nice and clean. The day we want to return is the offset after logic applied above.
    # and the month we want to return is the index we end up with at the end of the loop.
    day_to_return = days_offset
    month_to_return = month_index
    return day_to_return, month_to_return


# Add x days to the given date, then return it.
def add_days_to_a_date(initial_date, initial_month, initial_year, days_to_add):
    offset_from_start_of_year = offset_days_from_start_of_year(initial_date, initial_month, initial_year)

    if is_leap_year(initial_year):
        remaining_days_in_year = 366 - offset_from_start_of_year
    else:
        remaining_days_in_year = 365 - offset_from_start_of_year

    resulting_year = 0
    resulting_offset = 0

    if days_to_add <= remaining_days_in_year:
        # Base case, if you're not traveling more than a year, then your resulting year is this year
        # and your offset won't bleed into next year, and you can just add it.
        resulting_year = initial_year
        resulting_offset = offset_from_start_of_year + days_to_add
    else:
        # Otherwise, you need to calculate a bunch of stuff.
        days_to_add -= remaining_days_in_year
        resulting_year = initial_year + 1

        # Check if the NEXT year is a leap year.
        if is_leap_year(resulting_year):
            next_years_days = 366
        else:
            next_years_days = 365

        # Then loop through the rest of the years... God help us
        while days_to_add >= next_years_days:
            days_to_add -= next_years_days
            resulting_year += 1
            if is_leap_year(resulting_year):
                next_years_days = 366
            else:
                next_years_days = 365
        resulting_offset = days_to_add

    # Finally, we have the data we want. We can get the day and month we want from the resulting offset and year we just
    # calculated.
    day_returned, month_returned = date_from_offset(resulting_offset, resulting_year)

    return day_returned, month_returned, resulting_year


# From here https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Implementation-dependent_methods_of_Sakamoto.2C_Lachman.2C_Keith_and_Craver
def get_day_of_week_from_date_string(day, month, year):
    t = [0, 3, 2, 5, 0, 3,
         5, 1, 4, 6, 2, 4]
    year -= month < 3
    # Keep a days index and return the string of the day to be more bloody useful to me.
    days_index = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    index = ((year + int(year / 4) - int(year / 100) + int(year / 400) + t[month - 1] + day) % 7)
    return days_index[index]


def get_day_of_week_from_date_integer(day, month, year):
    t = [0, 3, 2, 5, 0, 3,
         5, 1, 4, 6, 2, 4]
    year -= month < 3
    index = ((year + int(year / 4) - int(year / 100) + int(year / 400) + t[month - 1] + day) % 7)
    return index


# For firstDate = "01/01/2015" , k = 2, daysOfTheWeek = ["Monday", "Thursday"], n = 4
print(solution("01/01/2015", 2, ["Monday", "Thursday"], 4))
