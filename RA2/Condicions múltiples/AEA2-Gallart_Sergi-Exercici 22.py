numero = int(input("Introdueix un nombre: "))

if numero % 2 == 0 and 10 <= numero <= 50:
    print("El nombre  és parell, està entre 10 i 50, i és més gran que 0.")
elif numero<=0:
    print("El número no és vàlid")
else:
    print("El nombre no compleix una de les condicions.")