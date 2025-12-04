#P026_RO047_algoritme3.py

s = 0
while s <= 100:
    x = int(input("x = "))
    if x > 0 and x < 10: # també: 0<x<10
        s = s + x
        print("s = ",s)
print("s = ", s)