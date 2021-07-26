def fun1(a, b, c):
    print('fun1(), a:', a)
    if a < b:
        a = 222
        return c
    else:
        a = 333
        return -c

def fun2(a):
    print('fun2(), a', a)
    #a = 111
    #print('fun2(), a', a)
    return 3*a + 1

def main():
    print('main(), a', a)
    print('fun1(10, 20, 30):', fun1(10, 20, 30))
    print('fun1(20, 10, 30):', fun1(20, 10, 30))
    for i in range(5):
        print('fun2(', i, '):', fun2(i))

a = 5  
main()
print('after calling main(), a:', a)
