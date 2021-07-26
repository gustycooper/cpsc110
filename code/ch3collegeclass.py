# collegeClass.py
# Determine the college class by number of credits

def main():
    print("Determin the college class by the number of credits.\n")
    credit = eval(input("Enter the number of credits: "))
    if credit < 7:
        clas = "Freshman"
    elif credit >= 7 and credit < 16:
        clas = "Sophomore"
    elif credit >= 16 and credit < 26:
        clas = "Junior"
    else:
        clas = "Senior"
    print("Class standing is " + clas)

main()
