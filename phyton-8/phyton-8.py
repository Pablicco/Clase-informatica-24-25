"""
datos = [5, 6, 7, 8, 9]
datos.append(15)
datos.append(20)


print("Imprimimos la primera y la tercer")
print(datos[0])
print(datos[2])

print("Imprimimos todo el array")
for i in range (0,len(datos)) :
    print(datos[i])

print("imprimimos el array al revés")
for i in range (len(datos)-1, -1, -1) :
    print(datos[i]) 

"""

datos = []

for i in range (0,5) :
    datos.append(int(input("Dame un número: ")))

for i in range (0,5) :
    print(datos[i])