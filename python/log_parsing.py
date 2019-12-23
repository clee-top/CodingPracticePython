# N-> This was from Glassdoor. Was a tech screen.

# Given input of host names of the pattern:
# ENV-DEPLOYMENT_ID-APP_NAME-INDEX.DOMAIN
# Report a tab separated table of
# ENV<TAB>APP_NAME<TAB>DEPLOYMENT_ID<TAB>COUNT_OF_HOSTS
#
# COUNT_OF_HOSTS is the number of hostnames of the same ENV, APP_NAME, and DEPLOYMENT_ID
#
# input = '''
# Prod-20160502-app-02.glassdoor.local
# Qa-20181001-app-02.glassdoor.local
# Qa-20181001-app-04.glassdoor.local
# Qa-20181002-myapp-01.glassdoor.local
# '''
#
# Expected Output
# Prod   app     20160502       1
# Qa     app     20181001       2
# Qa     myapp   20181002       1

import re

# This function takes some raw input files and outputs both a more formatted string as well
# as grouping entries that have the same "ENV" and "APP_NAME" entry.
def parse_log_file(input_string):

    # Keep a data structure that'll allow for counting.
    counts_dict = {}

    for line in input_string.splitlines():

        # Split the entry into components we care about.
        new_entry = re.split(r'[-.]', line)

        #print(new_entry[0])

        # If the entry already exists, just increment the value, keep the original text as the key.
        if str(new_entry[0]+new_entry[1]+new_entry[2]) in counts_dict:
            counts_dict[new_entry[0]+ " " + new_entry[1] + " " + new_entry[2]] += 1
        else:
            counts_dict[new_entry[0]+ " " + new_entry[1] + " " + new_entry[2]] = 1

    print(str(counts_dict))
    #for entry in counts_dict:
    #print(entry.split(" "))



example_log = '''Prod-20160502-app-02.glassdoor.local
Qa-20181001-app-02.glassdoor.local
Qa-20181001-app-04.glassdoor.local
Qa-20181002-myapp-01.glassdoor.local'''

parse_log_file(example_log)
