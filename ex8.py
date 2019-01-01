# Setting formatter to 4 empty arguments
formatter = "{} {} {} {}"

# Each print function uses format to pass 4 values into our variable.
print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

# This print funcion is no different than the others. Just split onto new lines.
print(formatter.format(
    " You think you're so smart\n",
    "with your fancy little words\n",
    "this is not so hard.\n",
    "- Sokka"
))