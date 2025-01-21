"""
6.5 Realiza un programa que lea dos números por teclado y permita elegir entre 4
opciones en un menú
1 - Mostrar la suma de los dos números
2 - Mostrar la resta de los dos números (el primero menos el segundo)
3 - Mostrar la multiplicación de los dos números
4 - Salir del programa
En caso de introducir una opción inválida, el programa volverá a solicitar otra
opción hasta que el usuario elija salir.
"""

n1 = int(input("Dame un número: "))
n2 = int(input("Dame otor número: "))


print("1 - Mostrar la suma de los dos números")
print("2 - Mostrar la resta de los dos números (el primero menos el segundo)")
print("3 - Mostrar la multiplicación de los dos números")
print("4 - Salir del programa")

x = int(input("Elige una opción de las cuatro: "))

while x != 1 or x != 2 or x != 3 or x != 4 :
    print("ups")
    x = int(input("Esa no es ninguna de las cuatro opciones, vuelve a introducir el número: "))
if x == 1 :
    print(n1 + n2)
elif x == 2 :
    print(n1 - n2)
elif x == 3 :
    print (n1 * n2)
else :
    print ("Fin del programa")
