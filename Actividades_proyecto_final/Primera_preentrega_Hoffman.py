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



def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Registro")
	print ("\t2 - Inicio de sesión")
	print ("\t3 - (Sólo admins) Ver usuarios del sistema")
	print ("\t0 - Salir")


while True:
	# Se muestra el menu
	menu()
    
	opcionMenu = input("Ingrese un número >> ")
    
	if opcionMenu=="1":
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
		almacenar(base_de_datos)
		
		#1break
	elif opcionMenu=="2":
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar");login(base_de_datos)
	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar");base_de_datos
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
