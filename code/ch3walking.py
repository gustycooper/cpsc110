print("Program to determine if someone is walking")
print("This solution nests an if-else statement in an else")
speed = int(input("Enter speed: "))
if speed < 3:
    print("Walking")
else:
    if speed >=3 and speed <= 5:
        print("Jogging")
    else:
        print("Running")

