#p004_ro025_paritmetica_01.py

a1 = 6
n = 1
d = 7/3

while n < 11:
    an = a1+(n-1) * d
    print ("a",n,"= ",round(an,2))
    n = n + 1
print ("a",n-1,"= ",round(an,2))