#P022_RO45_exemple4.py

a = int(input("a = "))
b = int(input("b = "))

x = 0

if a < 5:
    x = x + a - b
    print("x = ",x)
else:
    control = True
    while control == True:
        x = x + a
        while x < b:
            x = x + a
            print("x = ",x)
            #control = True
        control = False
    print("x = ",x)
        