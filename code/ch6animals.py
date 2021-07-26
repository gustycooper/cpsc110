def get_animal_years(filename):
    mal_mul_dict = {}
    infile = open(filename,"r")
    for line in infile:
        animal, multiplier = line.split()   # l is ['dog', '7.0']
        multiplier = float(multiplier)      # convert '7.0' to 7.0
        mal_mul_dict[animal] = multiplier
    infile.close()
    return mal_mul_dict

def process_commands(mal_mul_dict):
    while (True):
        line = input("Enter animal, people-years: ")
        if line == 'q':
            break
        animal, peopleyears = line.split(",")
        peopleyears = int(peopleyears)
        if animal in mal_mul_dict:
            animalyears = peopleyears * mal_mul_dict[animal]
            print(animal, "is", animalyears, "people-years.")
        else:
            print(animal, "not found.")

def main():
    print("Animal Program - Converts people-years to animal-years")
    print("Enter q at prompt to quit")
    mal_mul_dict = get_animal_years('ch4animals.txt')
    process_commands(mal_mul_dict)

main()
