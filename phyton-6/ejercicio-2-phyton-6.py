code = input("Escribe el código: ")
clave = int(input("Escribe la clave: "))

while (clave != 0987) or (code != "admin") :
    print("Ups algo ha ido mal, vuelve a intentarlo")
    code = input("Escribe el código: ")
    clave = int(input("Escribe la clave: "))
print("Código y contraseña correctos :)")
