"""
EJERCICIO 1
Escribe un programa que imprima todos los números pares entre dos
números que se le pidan al usuario.

Pablo Esquembre Amorós - 5/2/2025
"""

#primero pido dos números
n1 = int(input("Dame un número: "))
n2 = int(input("Dame otro número: "))

print("Los números pares que hay entre esos dos números(en orden ascendente) son:")

"""
antes de nada tengo que determinar si el primer número es mayor o menor que el segundo con el comado if,
luego usaré un método u otro (dependiendo de si n1 es mayor o menor que n2) para mostrar los números que 
hay entre esos dos, para ello, defino con el comando for-in-range y la variable i los números que se 
encuetran entre entre n1 y n2. Finalmente, muestro solo los pares con el comando if sabiendo que si 
x entre dos da un número entero, x es par
"""

if n1 < n2:
    for i in range(n1,n2 + 1):
        if i % 2 == 0:
            print(i)   
else :
    for i in range(n2,n1 + 1):
        if i % 2 == 0:
            print(i)   