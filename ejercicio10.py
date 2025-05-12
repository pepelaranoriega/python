mayor = None
menor = None
for i in range (1, 11):
    numero = int(input ("Ingresa numero: "))
    if mayor is None and menor is None:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero


print(f"El número mayor es: {mayor}, y el numero menor es  {menor}")