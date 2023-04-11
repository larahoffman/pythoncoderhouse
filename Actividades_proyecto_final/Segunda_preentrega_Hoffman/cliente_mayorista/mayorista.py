from base_cliente.cliente import Cliente

class ClienteMayorista(Cliente):
    def __init__(self, numero, nombre, correo, telefono, puntos):
        super().__init__(numero, nombre, correo, telefono)
        self.puntos = puntos
    
    def __str__(self):
        return f"{super().__str__()}\nCantidad de puntos: {self.puntos}"