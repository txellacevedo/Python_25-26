#P005_RO025_repte.py
#resultat dels reptes assolits d'una matèria

repte= int(input("repte sobre 100 punts: "))
unitats = int(input("unitats sobre 10 punts:"))
tasca1 = int(input("resultat de la tasca 1 sobre 10:"))
tasca2 = int(input("resultat de la tasca 2 sobre 10:"))          
tasca3 = int(input("resultat de la tasca 3 sobre 10:"))

tasques = (tasca1 + tasca2 + tasca3)/3
nr = 0.7*repte
nu = 0.2*unitats*10
nt = 0.1*tasques*10
nf = nr + nu + nt

print("nf = ",nf)