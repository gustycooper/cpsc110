fname = input("Enter filename: ")
infile = open(fname,"r")
for line in infile:
    print(line)
for c in line:
    print(ord(c),sep=' ',end=' ')
print()
infile.close()

fname = input("Enter filename: ")
infile = open(fname,"r")
for line in infile.readlines():
    print(line)
for c in line:
    print(ord(c),sep=' ',end=' ')
print()
infile.close()

fname = input("Enter filename: ")
infile = open(fname,"r")
data = infile.read()
print(data)
for c in data:
    print(ord(c),sep=' ',end=' ')
print()
infile.close()

fname = input("Enter filename: ")
infile = open(fname,"r")
x = infile.readline()
while x != "":
    print(x)
    y = x
    x = infile.readline()
for c in y:
    print(ord(c),sep=' ',end=' ')
print()
infile.close()
