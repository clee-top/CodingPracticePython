## Solution

Note: words.txt is the example the company gave.

cat <target text file> | tr ' ' '\n' | sed '/^[[:space:]]*$/d' | sort | uniq -c | sed 's/^[ \t]*//;s/[ \t]*$//' | sort -n -r | awk '{print $2,$1}'

Explanation (By command) -> 
cat (Concatenate) - Gets the text from file and is now in your output stream. Piped to next command, as are all the other pipes.

tr (translate) - Used to replace whitespace characters with newlines. This makes it so every word is on its own line alone.

sed (stream editor) - Edits input streams. Got this the filter from Google which strips blank lines. 

sort - Now the input is easy to sort which by default puts it in alphabetical order grouped with all of its duplicates.

uniq - Strips away duplicates. It also gives you the count of each word with the "-c" flag which is the crux of what the problem wants.

sed(stream editor) - Again to strip whitespace for the next command.

sort - We want to sort the remaining input by number in reverse order to get the output the way the problem wants.

awk - Simple awk program that just gets two input on every line and switches the first and second field which effectively reverses the order to get the order what we want.
