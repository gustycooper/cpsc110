print("Program to students and bicycles.")
print("At name prompt, enter a name or q to quit.")
print("At bicycle prompt, enter yes, y, no, or n.")

nameprompt = "Enter Name: "
bicycleprompt = "Do you own a bicycle: "
numstudents = 0
numstudentsownbicycles = 0
while True:
    name = input(nameprompt)
    if (name == "quit" or
        name == "Quit" or
        name == "q"    or
        name == "Q"):
        break
    numstudents = numstudents + 1
    ownbicycle = input(bicycleprompt)
    if ownbicycle == "yes" or ownbicycle == "y":
        numstudentsownbicycles += 1

print("Num Students:", numstudents,
      ", Num Students Own Bicycles:", numstudentsownbicycles)
