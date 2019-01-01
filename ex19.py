# Creates a function that prints information to the terminal.
# We use 2 arguments for this function and use f-strings to give the info.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")

# Calls the function and passes in integers for bot arguments
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")

# Setting up variables to use for our function
amount_of_cheese = 10
amount_of_crackers = 50

# Calls the function and passes the above variables to it.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")

# Calls the function and passes 2 math equations as the arguments.
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")

# Calls the function and passes both variables added to another number.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
