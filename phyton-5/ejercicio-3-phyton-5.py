n = int(input("Dime un año: "))

if (n % 400) == 0 :
    print(n, "es un año bisiesto")
elif (n % 100) == 0 :
    print(n, "no es un año bisiesto")
elif (n % 4) == 0 :
    print(n, "es un año bisiesto")
else :
    print(n, "no es un año bisiesto")