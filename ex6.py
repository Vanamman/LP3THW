
# Assigning 10 to types_of_people.
types_of_people = 10

# Assigning a variable to an f-string that uses the above variable in it.
x = f"There are {types_of_people} types of people."

# Assigning a string to 2 variables
binary = "binary"
do_not = "don't"

# Using the above variables in an f-string to assign to a new variable.
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# Using f strings to insert variables into a string and print them.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assigning hilarious to a boolean value of False.
hilarious = False

# Assigning a string to joke_evaluation.
joke_evaluation = "Isn't that joke so funny?! {}"

# Printing joke_evaluation and formatting it to use the variable hilarious.
# Like an f-string, but different.
print(joke_evaluation.format(hilarious))

# Assigning two variables seperate strings.
w = "This is the left side of..."
e = " a string with a right side."

# Concatenating both variables w and e together. Forming a single string.
print(w + e)