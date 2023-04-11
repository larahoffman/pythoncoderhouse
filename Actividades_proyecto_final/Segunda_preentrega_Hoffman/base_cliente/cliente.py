# Clase padre
class Cliente:
    def __init__(self, numero, nombre, correo, telefono):
        self.numero = numero #este valor podría ser random
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"El cliente número {self.numero} se llama {self.nombre}, su correo es {self.correo} y su teléfono es {self.telefono}."
    
    # Por si se quisiera modificar el numero de contacto
    def cambiar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def enviar_correo(self):
        print(f"Enviando correo a {self.correo}\n...")