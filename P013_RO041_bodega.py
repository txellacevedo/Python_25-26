n = int(input("Cantidad de paquetes: "))

mayor = -1

for i in range(n):
    peso = float(input(f"Peso del paquete {i+1}: "))
    if peso > mayor:
        mayor = peso

print("El mayor peso es:", mayor)
