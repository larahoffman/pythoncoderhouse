class Cliente:
    def __init__(self, numero, nombre, edad, correo, telefono):
        self.numero = numero #este valor podría ser random
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"El cliente número {self.numero} se llama {self.nombre}, su correo es {self.correo} y su teléfono es {self.telefono}."