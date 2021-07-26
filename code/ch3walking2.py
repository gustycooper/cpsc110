print("Program to determine if someone is walking")
print("This solution uses a 3-way if-elif-else statement")
speed = int(input("Enter speed: "))
if speed < 3:
    print("Walking")
elif speed >=3 and speed <= 5:
    print("Jogging")
else:
    print("Running")
