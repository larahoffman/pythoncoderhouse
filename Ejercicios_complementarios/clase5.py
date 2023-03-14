# Ejercicio 1

# Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.


n1 = int(input("Ingrese un número: "))
n2 = int(input("Ahora, ingrese otro número: "))
n = int(input("Elija un numero del 1 al 4: "))

i = 0
while n<=4:
    if n > 0 and n<=3: # yo se que se puede mejorar
        print(n1+n2)
        print(n1-n2)
        print(n1*n2)
        n = int(input("Elija un numero del 1 al 4: "))
    else:
        break
else:
    print("La opcion ingresada no es valida")
i += 1


# Ejercicio 5

# Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo.
# La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

lista = [0,1,2,3,4,5,6,7,8,9]

nro = int(input("Ingrese un numero entero del 0 al 9: "))

i = 0

while ((nro in lista) != True):
    print("El valor ingresado es incorrecto")
    nro = int(input("Ingrese un numero entero del 0 al 9: "))
else:
    print("Su numero es", nro)

i += 1


# Ejercicio 6

# Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

# La conversión de listas es mi_lista=list(range(inicio,fin,salto))

lista_cero_diez = list(range(0,11))

lista_cero_diez_negativa = list(range(-10,1))

lista_cero_veinte_pares = list(range(0,21,2))

lista_uno_diecinueve_negativa = list(range(-19,1,2))

lista_multiplos_cinco = list(range(0,51,5))

print(lista_cero_diez)
print(lista_cero_diez_negativa)
print(lista_cero_veinte_pares)
print(lista_uno_diecinueve_negativa)
print(lista_multiplos_cinco)