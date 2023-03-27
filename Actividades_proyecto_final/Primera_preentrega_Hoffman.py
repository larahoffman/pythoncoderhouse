import json
import os

def cargar_base_de_datos():
    if os.path.exists('base_de_datos.json'): # Busca primero si el archivo json existe
        with open('base_de_datos.json', 'r') as file:
            base_de_datos = json.load(file)
    else:
        base_de_datos = {}
        with open('base_de_datos.json', 'w') as file:
            json.dump(base_de_datos, file, indent=4)
    return base_de_datos

def almacenar(base_de_datos):
    print('|-------------- Registro --------------|')
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    print('|--------------------------------------|')

    if user in base_de_datos:
        print(f"El usuario {user} ya existe.")
    else:
        base_de_datos[user] = password

        with open('base_de_datos.json', 'w') as file:
            json.dump(base_de_datos, file, indent=4)

def login(base_de_datos):
    print('|---------- Inicio de sesión ----------|')
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    print('|--------------------------------------|')
    if user in base_de_datos:
        if base_de_datos[user] == password:
            print('')
            print(f"Bienvenidx, {user}")
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
    else:
        print("El usuario ingresado no existe.")

# Cargar la base de datos
base_de_datos = cargar_base_de_datos()

# Ejecutar la función de almacenamiento de usuarios y contraseñas
almacenar(base_de_datos)

# Ejecutar la función de inicio de sesión
login(base_de_datos)
