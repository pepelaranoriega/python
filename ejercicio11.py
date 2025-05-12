for i in range (1, 4):
    password = input("Ingresa la contraseña:")
    passwordconfirm = input("Repite la contraseña: ")

    if password == passwordconfirm:
        print("contraseña aceptada")
        break
    else:
        print(f"las contraseñas no coinciden. Intento {i} de 3")
    if i == 3:
        print(f"se acabaron los intentos!!!")



