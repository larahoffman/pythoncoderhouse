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


