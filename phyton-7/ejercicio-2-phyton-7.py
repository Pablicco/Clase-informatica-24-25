"""
7.2 Pide al usuario un número entero (por ejemplo, 5) y muestra la tabla de
multiplicar de ese número( Ejemplo: “5 x 1 = 5” hasta “5 x 10 = 50”)
"""

n = int(input("Dame un número: "))

for x in range(1,11) :
    print(n, "x", x, "=", n*x)