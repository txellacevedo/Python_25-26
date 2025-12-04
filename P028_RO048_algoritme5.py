#P028_RO048_algoritme5.py

a, b = int(input("a = ")), int(input("b = "))

if a < 0:
    if b < 0:
        b = 2 * b
    else:
        while True:# també b >=0, bucle infinit!!!
            b = b + 1
            print("a = ",a,"b = ",b)
else:
    a = a + 1
    b = b - 1
    while a < b:
        a = a + 1
        b = b - 1
        print("a = ",a,"b = ",b)
print("a = ",a,"b = ",b)