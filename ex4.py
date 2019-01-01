# Number of cars in the lot
cars = 100

# Number of people the car can fit
space_in_a_car = 4.0

# Number of drivers available
drivers = 30

# Number of passengers for the day
passengers = 90

# Numbers of cars not in use based on how many drivers we have compared to cars
cars_not_driven = cars - drivers

# Numbers of cars in use based on the number of drivers available.
cars_driven = drivers

# Number of available seats for the day.
carpool_capacity = cars_driven * space_in_a_car

# Number of passengers per car for the day
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")