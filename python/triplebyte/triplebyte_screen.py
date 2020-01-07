
# Description from Triplebyte Proctor
# Big log file, all the questions are stuff you want to know about them

import re

# This function parses the log file and returns how many of the requests gave a 404.
def response_not_found():

    file_name = "apache_logs"
    log_file = open(file_name, "r")

    first_line = log_file.readline()

    #print("The first line is: " + first_line)
    # first_split = re.split(r'\w', first_line)
    # first_split = first_line.split()
    # print("The split of the first line on whitespace is: " + str(first_split))
    # print("The response code is: " + str(first_split[6]))

    not_found_counter = 0
    for line in log_file:
        # Go through each line and cut out the response code, count it.
        split_line = line.split()
        if split_line[6] == "404":
            not_found_counter +=1

    print("We found this many 404 codes: " + str(not_found_counter))
    return not_found_counter

# Get the unique ips
def unique_ips():

    file_name = "apache_logs"
    log_file = open(file_name, "r")

    first_line = log_file.readline()

    unique_set = set()

    not_found_counter = 0
    for line in log_file:
        # Go through each line and cut out the response code, count it.
        split_line = line.split()
        if split_line[0] not in unique_set:
            unique_set.add(split_line[0])

    unique_count = len(unique_set)

    print("We found this many unique ips: " + str(unique_count))
    return unique_count

# Get all the bytes in responses.
def size_response():

    file_name = "apache_logs"
    log_file = open(file_name, "r")

    # Store every response of the appropriate date.
    bytes_on_date = 0

    for line in log_file:
        split_line = line.split()
        if "[18/May/2015" in line:
            # Dash means no data sent
            if split_line[7] == "-":
                continue
            # You found the date, count the bytes.
            # print("The bytes on this date are: " + str(split_line[7]))
            bytes_on_date += int(split_line[7])

    print("Bytes on date responses: " + str(bytes_on_date))
    return bytes_on_date

# Get top five resources accessed (Urls)
def top_five():
    file_name = "apache_logs"
    log_file = open(file_name, "r")

    # Store every response of the appropriate date.
    bytes_on_date = 0

    request_dict = {}

    for line in log_file:
        split_line = line.split()
        print("Get the resource! " + str(split_line[4]))

    print("Bytes on date responses: " + str(bytes_on_date))
    return bytes_on_date

# response_not_found()
# unique_ips()
# size_response()
# Get the top five responses.
# top_five()
# Find the busiest thirty minute window.
# thirty_minute_window()

# Bonus  -> Scan the logs and see any security issues. I saw a bunch of logs trying to access admin page and reset passwords. That's bad.