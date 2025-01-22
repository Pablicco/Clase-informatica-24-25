"""
6.4 Árbol de navidad en Python. Imprime un árbol de navidad formado con *
haciendo uso del while y de la multiplicación de un entero por una cadena,
cuyo resultado en Python es replicar la cadena.
#      *
#     ***
#    *****
#   *******
#  *********
# ***********
"""

x = "*"
e = " "
l = 1
n = int(input("Dame un número: "))
while n > 0 :
    print((n - 1) * e, x * l, (n - 1) * e)
    n = (n - 1)
    l = (l + 2)
print("Feliz Navidad")
