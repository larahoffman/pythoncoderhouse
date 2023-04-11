from base_cliente.cliente import *
from cliente_mayorista.mayorista import ClienteMayorista
from cliente_minorista.minorista import ClienteMinorista
from primera_preentrega.funciones_menu import *

cliente1 = ClienteMayorista(1, "Murisco Company", "contacto@murisco.com.ar", "11-33765091", 1000)
cliente2 = ClienteMinorista(2, "Juan Perez", "juano@gmail.com", "11-54338976", 5)
cliente3 = ClienteMinorista(3, "Estela Martinez", "stella123@hotmail.com", "11-77832122", 10)

menu()
if opcionMenu=="4":

    print("Clientes")
    print("")
    print("Sección mayorista:")
    print(cliente1)
    print("")
    print("Sección minorista:")
    print(cliente2)
    print(cliente3)
    print("")
    print("Acciones:")
    cliente1.enviar_correo()
    cliente2.cambiar_telefono("11-44536166")

    print(f"El nuevo número de télefono del cliente {cliente2.nombre} es: {cliente2.telefono}")
    