import secrets
import string
import sys


def generar_contrasena(longitud):
    # Definimos los caracteres permitidos para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generamos una cadena aleatoria de la longitud especificada
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

def continuar_tarea(tarea):
    try:
        tarea = tarea.upper()
        if tarea == "Y":
            contraseña = int(input("Longitud: "))
            contrasena_generada = generar_contrasena(contraseña)
            print(f"Contraseña generada: {contrasena_generada}")
            return False
        elif tarea == "N":
            sys.exit(0)
        else:
            print("No has ingresado las letras N o Y")
            return True
    except ValueError:
        print("No ingresaste un numero entero.")

# Generar una contraseña de 20 caracteres
ok = True
while ok:
    try:
        contrasena = int(input("Longitud: "))
        contrasena_generada = generar_contrasena(contrasena)
        print(f"Contraseña generada: {contrasena_generada}")
        ok = False
    except ValueError:
        print("No ingresaste un numero entero.")
letra = True
while letra:
    respuesta = input("Quieres crear otra contraseña? (Y/N): ")
    letra = continuar_tarea(respuesta)