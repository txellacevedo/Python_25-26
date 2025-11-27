#P004_RO25_Paritmetica_03
#exercici 15 llibre de mates
#progressions aritmètiques _ exercici global

"""
comentaris amb cometes
comentaris més llargs, per exemple bocins de codi
"""

a1 = -203
an = 902.5 #terme enessim
d = 16.5

n = ((an - a1) / d) + 1
print("n = ",n)
print () #linea lliure, sense res

k = n

n = 1
s = 0
print("n       a              s        \n") #el \n vol dir separacio

while n < k+1:
    a = a1 + (n - 1) * d
    s = a + s
    print(n,"     ",a,"         ",         s)
    #prints(s, end = " ")
    n = n +1






