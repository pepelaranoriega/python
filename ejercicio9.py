pares = 0
impares = 0
for i in range (1, 11):
    numero = int(input ("Ingresa numero: "))


    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Hay {pares} numero pares y hay {impares} numeros impares")
