# Imports argv from the system module
from sys import argv

# Establishes the # of arguments needed to run program
script, filename = argv

# Assigns a variable to open the filename argument.
txt = open(filename)

# Tells you the name of the file
print(f"Here's your file {filename}")

# Prints the file to the shell
print(txt.read())
txt.close()

# Asks you to type the filename again.
# Can type any filename however
print("Type the filename again:")

# Prompt for the filename and assigns it to a new variable.
file_again = input("> ")

# Opens the file and assigns it to a new variable
txt_again = open(file_again)

# Prints the file to the shell.
print(txt_again.read())
txt_again.close()