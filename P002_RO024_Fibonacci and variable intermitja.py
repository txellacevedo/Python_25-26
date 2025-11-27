#POO2_R
anterior = 0
fibonacci = 1
maxim = 100


print("series de fibonacci dels ", maxim , "primer nobres\n")
print(0, fibonacci, end = " ")


while fibonacci < maxim:
    x= fibonacci # x - - variable intermitja
    fibonacci = fibonacci + anterior
    anterior = x
    print(fibonacci)

anterior = 0
fibonacci = 1
maxim = 100
fibonacci_seguent = 1

