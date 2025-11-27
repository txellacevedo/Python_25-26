#pOO2_ROO25_cilindre

pi = 3.1416
radi = int(input("radi= "))
# radi = 25
# altura = 36
altura = int(input("altura = "))
print("Àrea i volum d'un cilindre. Dades en cm")
# volum = pi * radi * radi * altura
# volum = pi * radi**2 * altura
volum = pi * pow(radi,2) * altura

print("volum = ",volum,"cm3")