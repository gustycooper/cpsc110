print("Animal Program - Converts people-years to animal-years")
print("Enter q at prompt to quit")
animals = []
multipliers = []
infile = open('ch4animals.txt',"r")
for line in infile:
    l = line.split()        # l is ['dog', '7.0']
    l[1] = float(l[1])      # convert '7.0' to 7.0
    animals.append(l[0])
    multipliers.append(l[1])

while (True):
    line = input("Enter animal, people-years: ")
    if line == 'q':
        break
    l = line.split(",")
    animal = l[0]
    peopleyears = int(l[1])
    found = False
    for i in range(len(animals)):
        if animal == animals[i]:
            animalyears = peopleyears * multipliers[i]
            print(animal, "is", animalyears, "people-years.")
            found = True
            break
    if not found:
        print(animal, "not found.")

