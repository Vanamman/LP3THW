name = "Tim D. Ott"
age = 29
height = 72 #inches
weight = 225 # lbs
eyes = "Hazel"
teeth = 'White'
hair = 'Brown'

centimeters = round(height * 2.54)
kilograms = round(weight * 0.45359237)

print(f"\nLet's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print(f"His height is centimeters is {centimeters}.")
print(f"His weight in kilograms is {kilograms}. \n")