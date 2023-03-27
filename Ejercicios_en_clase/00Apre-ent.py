
usuario = 'juan'
passwd = 'juan'

# ...

# conexion = conectar_con_servicio(usuario, passwd)

# # hacemos algo con la conexion
# ...

# usuario = input("Ingrese su usuario: ")
# passwd = input("Ingrese su pass: ")

file = open("secreto.cfg", "w")
file.write(usuario  + "\n")
file.write(passwd  + "\n")
file.close

file = open("secreto.cfg", "r")
# content = file.read()
with open('secreto.cfg', 'r') as secreto:
    usuario = secreto.readline().strip()
    passwd = secreto.readline().strip()
file.close


# print(f'{content=}')
print(f'{usuario=}')
print(f'{passwd=}')

correcto=False

while correcto==False:
        nombre=input("Ingrese nombre de usuario: ")
        if usuario == nombre:
            print("Usuario existe")
            correcto=True
        else:
            print ("Usuario no existe")
            break

while correcto==True:
    contrasenia=input("Ingrese su Password: ")
    if passwd==contrasenia:
        print("Usuario y contraseñas correctas")
        correcto=False
    else:
        print("Usuario y/o contraseñas no existe")
        break
    
