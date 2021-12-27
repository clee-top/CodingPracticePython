# Parse this sort of log file into a csv looking format.
# N -> Didn't have time to sort it, but otherwise correct. Could've shoved the ID as the dictionary entry, sorted, re-added to string.
# This was a question from Brex

# N -> Splits and respects substrings by default, savage. https://docs.python.org/3/library/shlex.html
# N -> https://stackoverflow.com/questions/79968/split-a-string-by-spaces-preserving-quoted-substrings-in-python
import shlex

txt = """timestamp="Wed Jun 19 09:35:36 PDT 2019" message="test 10" id=10 field_1="test 10" field_6="test 1"
timestamp="Wed Jun 19 09:35:37 PDT 2019" message="test 4" id=4 field_2="test 4"
timestamp="Wed Jun 19 09:35:38 PDT 2019" message="test 2" id=3 field_3="test 2" field_9="test 23"
timestamp="Wed Jun 19 09:35:39 PDT 2019" message="test 3" id=2 field_4="test 3"
timestamp="Wed Jun 19 09:35:40 PDT 2019" message="test 4" id=1 field_5="test 4"
timestamp="Wed Jun 19 09:35:37 PDT 2019" message="test 5" id=5 field_3="test 10"
timestamp="Wed Jun 19 09:35:40 PDT 2019" message="test 6" id=6 field_1="test 5"
"""


# id,timestamp,message,field_1,field_2,field_3,field_4,field_5,field_6,field_9
# 1,"Wed Jun 19 09:35:40 PDT 2019","test 4",,,,,"test 4",,
# 2,"Wed Jun 19 09:35:39 PDT 2019","test 3",,,,"test 3",,,
# 3,"Wed Jun 19 09:35:38 PDT 2019","test 2",,,"test 2",,,,"test 23"
# 4,"Wed Jun 19 09:35:37 PDT 2019","test 4",,"test 4",,,,,
# 5,"Wed Jun 19 09:35:37 PDT 2019","test 5",,,"test 10",,,
# 6,"Wed Jun 19 09:35:40 PDT 2019","test 6","test 5",,,"test 5",,
# 10,"Wed Jun 19 09:35:36 PDT 2019","test 10","test 10",,,,,"test 1",

# Duple id's? No.

def parse_logs_to_csv(input_log):
    # Split the lines to iterate over them.
    split_lines = str.splitlines(input_log)
    return_string = ""

    for line in split_lines:
        # Parse each line and populate the dictionary.
        # print("The line looks like this: " + line)

        # Split and ignore quoted substrings.
        split_fields = shlex.split(line)
        # print("The split fields look this this: " + str(split_fields))
        # print("The ID is always in the same place and it is here: " + str(split_fields[2]))

        # Not in the order I want, pre-do this then the fields.
        csv_line = str(split_fields[2].split("=")[1] + ",") + str(split_fields[0].split("=")[1] + ",") + str(split_fields[1].split("=")[1] + ",")
        # print("The Test CSV Line is: " + csv_line)

        length_of_split = len(split_fields)
        # print("My test length is " + str(length_of_split))

        # Iterate over the fields,
        for counter in range(3, length_of_split):
            csv_line += str(split_fields[counter].split("=")[1] + ",")
            # print("My field is: " + str(split_fields[counter].split("=")[1] + ","))

        print("Possible finished csv line looks like this: " + csv_line)
        return_string += csv_line
        # csv_dict[str(split_fields[2])] = [split_fields[0].split("=")[1], split_fields[1].split("=")[1]]
        # print("First test entry is: " + str(csv_dict[str(split_fields[2])]))
    return return_string


parse_logs_to_csv(txt)
