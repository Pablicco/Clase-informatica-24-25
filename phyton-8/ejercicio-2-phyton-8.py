datos = []

for i in range(0, 10):
    datos.append(int(input("Dame un número: ")))

print("Te muestro los pares")
for n in range(1, 10, 2):
    print(datos[n])