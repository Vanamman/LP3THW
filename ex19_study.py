def party(balloons, alcohol):
    print(f"You have {balloons} balloons!")
    print(f"You have {alcohol} bottles of alcohol!")
    print("That is a lot of balloons and alcohol!")
    print("This will be a great party!\n")

party(10,15)

balloons = 50
alcohol = 30

party(balloons, alcohol)
party(balloons + 5, alcohol - 5)
party(balloons * 4, alcohol)
party(25 + 30, 15 + 15)

party(input("How many ballons did you bring? "), 
input("How many bottles of alcohol did you bring? "))

party(0,0)