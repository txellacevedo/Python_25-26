#P008_RO028_for_n imparells.py
#verifictar que la suma dels primer n imparells és iguals
from math import *
n = int(input("numero d'imparels:"))
suma = 0

for i in range(1,n+1):
    k = (2 * i) -1
    suma = suma + k
print( "suma = ",suma)
if suma == pow(n,2):
    print("verdader")
else:
    print("fals")
