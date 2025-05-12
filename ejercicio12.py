suma_aprobatoria = 0
contador_aprobatoria = 0

for i in range (1, 6):
    calificacion = float(input("Ingrese las calificaciones: "))

    if calificacion >= 6:
        suma_aprobatoria += calificacion
        contador_aprobatoria += 1

if contador_aprobatoria > 0:
    promedio = suma_aprobatoria / contador_aprobatoria
    print (f"El promedio de calificaciones aprobadas es de {promedio:.2f}")
else:
    print(f"No hay calificaciones aprobatorias")