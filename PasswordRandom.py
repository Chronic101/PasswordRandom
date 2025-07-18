import secrets
import string
import sys

# Funcion para generar la contraaseña
def generar_contrasena(longitud):
    # Se definen los caracteres permitidos para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Se genera una cadena aleatoria con la longitud especificada
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena

# Funcion para seguir creando mas contraseñas despues de preguntarle al usuario
def continuar_tarea(tarea):
    try:
        tarea = tarea.upper()
        if tarea == "Y":
            contraseña = int(input("Longitud: "))
            contrasena_generada = generar_contrasena(contraseña)
            print(f"Contraseña generada: {contrasena_generada}")
        elif tarea == "N":
            sys.exit(0)
        else:
            print("No has ingresado las letras N o Y")
    except ValueError:
        print("No ingresaste un numero entero.")
    return True

# Se genera una contraseña de N caracteres
ok = True
while ok:
    try:
        longitud = int(input("Longitud: "))
        contrasena_generada = generar_contrasena(longitud)
        print(f"Contraseña generada: {contrasena_generada}")
        ok = False
    except ValueError:
        print("No ingresaste un numero entero.")

# Se le pregunta al usuario si quiere crear otra contraseña 
estado = True
while estado:
    respuesta = input("Quieres crear otra contraseña? (Y/N): ")
    estado = continuar_tarea(respuesta)