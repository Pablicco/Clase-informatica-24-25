"""
6.4 Pide al usuario su nombre y un número. Después de esto, muestra por
pantalla, su nombre el número de veces que haya elegido. Comprueba y evita
que se produzcan errores.
"""

nombre = input("Dame tu nombre: ")
n = int(input("Dame un número: "))

while n > 0 :
    print(nombre)
    n = (n - 1)
print("fin del programa")
