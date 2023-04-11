from base_cliente.cliente import *
from cliente_mayorista.mayorista import ClienteMayorista
from cliente_minorista.minorista import ClienteMinorista
# from primera_preentrega.funciones_menu import menu 

cliente1 = ClienteMayorista(1, "Murisco Company", "contacto@murisco.com.ar", "11-33765091", 1000)
cliente2 = ClienteMinorista(2, "Juan Perez", "juano@gmail.com", "11-54338976", 5)

print("Datos:")
print("")
print(cliente1)
print("")
print(cliente2)
print("")
print("Acciones:")
cliente1.enviar_correo()
cliente2.cambiar_telefono("11-44536166")

print(f"El nuevo número de télefono del cliente {cliente2.nombre} es: {cliente2.telefono}")