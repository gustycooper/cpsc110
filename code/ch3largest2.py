print("Program to determine largest number entered.")
print("At each prompt, enter a number or q to quit.")
prompt = "Enter>>> "
largest = "no value"
while True:
    value = input(prompt)
    if value == 'q':
        break
    if largest == 'no value':
        largest = int(value)
    elif largest < int(value):
        largest = int(value)
print("Largest number entered is", largest)
    
