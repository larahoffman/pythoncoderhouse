# Manejo de archivos

ruta = "C:/Proyecto Python/Ejercicios_en_clase"
f = open(ruta+'/archivo.txt', 'w')
f.write('Esto es un ejemplo')
f.close()

# # Primer ejercicio

file = open('misHobbiesFavoritos', 'w')

for i in range(3):
    variable = input('Ingrese su hobbie favorito: ')
    file.write(variable)

file.close()

# ------------------------------------------------------- #

