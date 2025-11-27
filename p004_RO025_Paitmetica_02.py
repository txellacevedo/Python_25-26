
# Programa para mostrar todos los términos de una progresión aritmética

a1 = 12
d = 5
n = 1
termino = a1

# Bucle para mostrar los términos
while n <= 32:
    an = a1+(n-1) * d
    print(termino, end=" ")  # end=" " hace que se muestren seguidos
    termino += d
    n = n + 1

# Mostrar el último término
print("\nEl último término de la progresión aritmética es:", termino - d)
