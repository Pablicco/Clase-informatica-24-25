datos = []
for i in range(0,5):
    datos.append(int(input("Dame un número: ")))

n = 0

while n < 6:
    if datos[n] % 2 == 0:
        print(datos[n])
        n = n+1
    else:
        n = n+1
print("fin")