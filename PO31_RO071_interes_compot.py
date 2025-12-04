#PO31_RO071_interes_compot.py

from math import log
"""
a= valor acumultat despres de posar n diposits
p =VALOR DE CADA DIPOSIT MENUSAL EN EUROS
x= valor nominal de l'interes menusal
n= numero de diposis menusal realitzats
"""
#apartat a
x= 0.04/12
p=300
n = 12*15
a = p * (((1+x)**n)-1)/x
print("valor acumultat = ", a)

#apartat b
x= 0.04/12
n=12*20
a=200000
p= a/((((1+x)**n)-1)/x)
print("valor de cada diposti mensuak p=  ",p )