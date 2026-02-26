num1=int(input("Escriu el primer número "))
num2=int(input("Escriu el segon número "))
num3=int(input("Escriu el tercer número "))

if num1>num2 and num1>num3:
    print(f"El primer número és el més gran dels tres")
elif num2>num1 and num2>num3:
    print(f"El segon número és el més gran dels tres")
else:
    print(f"El tercer número és el més gran dels tres")