print("Animal Program - Converts people-years to animal-years")
print("Enter q at prompt to quit")
mals_and_muls = []
infile = open('ch4animals.txt',"r")
for line in infile:
    l = line.split()        # l is ['dog', '7.0']
    l[1] = float(l[1])      # convert '7.0' to 7.0
    mals_and_muls.append(l)

while (True):
    line = input("Enter animal, people-years: ")
    if line == 'q':
        break
    l = line.split(",")
    animal = l[0]
    peopleyears = int(l[1])
    found = False
    for mal_and_mul in mals_and_muls:
        if animal == mal_and_mul[0]:
            animalyears = peopleyears * mal_and_mul[1]
            print(animal, "is", animalyears, "people-years.")
            found = True
            break
    if not found:
        print(animal, "not found.")
