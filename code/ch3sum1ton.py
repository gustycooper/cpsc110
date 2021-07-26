print("Sum of integers 1 to N")
n = int(input("Enter N: "))
count = 1
sum1toN = 0
while count <= n:
    sum1toN = sum1toN + count
    count = count + 1
print("Sum of 1 to", n, "is:", sum1toN)
