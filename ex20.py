from sys import argv

script, input_file = argv

# Creates a function that prints the entire passed file.
def print_all(f):
    print(f.read())

# Creates a function that seeks to the beginning of a file.
def rewind(f):
    f.seek(0)

# Creates a function that prints the line # and the content.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = '')


# Opens the file passed to argv
current_file = open(input_file)

print("First let's print the whole file:\n")

# Calls the print_all function on current_file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Seeks to the beginning of current_file
rewind(current_file)

print("Let's print three lines:")

# Sets current_line to 1 and prints the line # and content

# Better way to do the lines below using a while loop.

# current_line = 1
# while current_line < 4:
#     print_a_line(current_line, current_file)
#     current_line += 1

current_line = 1
print_a_line(current_line, current_file)

# Adds 1 to current_line and prints that line and content.

current_line += 1 # current_line = 2
print_a_line(current_line, current_file)

# Adds 1 to current_line again and prints the content.

current_line += 1 # current_line = 3
print_a_line(current_line, current_file)

