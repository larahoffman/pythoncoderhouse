# Se crea la clase Persona

class Persona:
    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Se crea el objeto persona_1 que es una instancia de la clase Persona

persona_1 = Persona("Pedro", 22)

print(f"La persona se llama {persona_1.nombre} y tiene {persona_1.edad} años.")