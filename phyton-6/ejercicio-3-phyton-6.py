"""
Escriba un programa que pregunte una y otra vez si desea continuar con el
#programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).
"""

n = input("¿Desea continuar con el programa?")

while n == "sí" :
    n = input("¿Desea continuar con el programa?")
print("Fin del programa")