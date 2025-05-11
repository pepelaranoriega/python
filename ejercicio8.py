numero = int(input("Ingresa un numero positivo: "))
if numero < 0:
    print(f"El numero tiene que ser positivo!")

else:
    factorial = 1
    for i in range (1, numero + 1):
        factorial *=i
print(f"El factorial de {numero} es {factorial}")

