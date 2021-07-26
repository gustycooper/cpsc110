print("Program to determine largest number entered.")
print("At each prompt, enter a number or q to quit.")
prompt = "Enter>>> "
value = input(prompt)
if value == 'q':
    print("Largest number entered is no value")
    quit()
largest = int(value)
while value != 'q':
    value = input(prompt)
    if value != 'q':
        intvalue = int(value)
        if intvalue > largest:
            largest = intvalue
print("Largest number entered is", largest)
