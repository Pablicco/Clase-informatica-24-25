"""
EJERCICIO 2
Escribe un programa que pida al usuario un número y muestre su raíz
cuadrada. Si el número introducido es negativo, se lo volverá a pedir
tantas veces como sea necesario hasta que introduzca uno positivo.

Pablo Esquembre Amorós - 5/2/2025
"""

#primero pido al usuario un número que será la variable n
n = int(input("Dame un número, te diré su raíz cuadrada: "))

#con el comando while, evito que el número sea negativo, ya que el usuario no saldrá del bucle hasta que n sea positivo
while n < 0:
    n = int(input("Ese número es negativo, introduzca otro por favor: "))
print("La raíz cuadrada de", n, "es", n**(1/2))
#definimos raíz cuadrada como un número elevado a 1/2