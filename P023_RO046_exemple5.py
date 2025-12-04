#P023_RO046_exemple5.py

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b:
    while c < a:
        c = c + 3
        print("c = ",c)
    print("c = ",c)
else:
    control = True
    while control == True:
        a = a + 5
        while a <= b + c:
            a = a + 5
            print("a = ", a)
        control = False
    print("a = ", a)
    print("c = ", c)