"""
#Programa que calcula la división entre dos números

dividendo = int(input("dividendo: "))
divisor = int(input("divisor: "))

while divisor == 0 :
    divisor = int(input("Dame otro divisor diferente a 0: "))
print("El resultado de la división es: ", dividendo / divisor)    

"""

#Programa que calcula la suma de n números

suma = 0
n = float(input("Dame un número:"))

while (n != 0) :
    suma = suma + n
    n = float(input("Dame otro número:"))
print ("La suma es: ", suma)