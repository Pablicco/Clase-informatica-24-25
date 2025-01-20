n = int(input("Dime un año: "))

if (n % 100) == 0 and (n % 400) != 0 or (n % 4) != 0:
    print(n, "no es bisiesto")
else :
    print(n, "es un año bisiesto")
