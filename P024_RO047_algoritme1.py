#P024_RO047_algoritme1.py

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

x = 0
y = 0

if not(a < 2 and b > 1) or (c > 3):
    x = a + b
else:
    y = b - c

print("x = ",x)
print("y = ",y)