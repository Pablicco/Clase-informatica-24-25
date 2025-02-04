datos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

n = int(input("Dame un número del 1 al 12: "))

while n > 13 or n < 0 :
    
    n = int(input("Ese número no está entre 1 y 12, prueba otra vez: "))

print(datos[n-1])