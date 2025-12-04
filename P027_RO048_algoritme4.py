#P027_RO048_algoritme4.py

a, b = int(input("a = ")), int(input("b = "))

if a > 0:
    if b < 100:
        t = 2 * a + b
    else:
        t = 0
else:
    t = 0

print("t = ", t)