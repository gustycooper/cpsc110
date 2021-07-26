# gcd.py
# Computes gcd of 2 numbers input by user

def main():
    print("Compute gcd of two nummbers.\n")
    m,n = eval(input("Enter two numbers separated by a comma: "))
    minput, ninput = m,n
    while m != 0:
        n,m = m, n%m
    print("gcd of", str(minput) + ",", ninput, "is", n)

main()
