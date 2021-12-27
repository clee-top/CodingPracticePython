infile = "test_file.txt"

important = []
keep_phrases = ["test",
                "important",
                "keep me"]

# Reference for with, it's like a free try catch -> https://docs.python.org/3/reference/compound_stmts.html#with
# Otherwise you have to .close the file.
# with open(infile) as f:
#    f = f.readlines()
# Open for reading!
new_file = open(infile, "r")

# Gets you all of them as a list of single lines. One single ass big string is returned with "read" and you can also for loop iterate with "readline" method.
file_text = new_file.readlines()

for line in file_text:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break

# Without the "with" magic above you'd want to f.close here.
new_file.close()


print(important)
