from base_cliente.cliente import Cliente

class ClienteMinorista(Cliente):
    def __init__(self, numero, nombre, correo, telefono, descuento):
        super().__init__(numero, nombre, correo, telefono)
        self.descuento = descuento
    
    def __str__(self):
        return f"Sección minorista:\n{super().__str__()}\nDescuento (en %): {self.descuento}"
