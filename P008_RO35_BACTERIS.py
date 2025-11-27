#P008_RO035_BACTERIS.py
n_bacteris = int(input("numero de bateris = "))
max_bacteris = int(input("numero maxim debacteris = "))
dia = 0 #condicions inicials


while n_bacteris <= max_bacteris :
    print("dia", dia, "n_bacteris =", n_bacteris)
    n_bacteris = n_bacteris * 2
    dia = dia + 1
print ("dia", dia, "n_bacteris = ", n_bacteris)