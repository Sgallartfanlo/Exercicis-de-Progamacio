edat=int(input("Introdueix la teva edat: "))
classificaciò=str(input("Has estat classificat en les últimes proves? Sí o No: "))
estat_físic=str(input("Introdueix el teu estat físic?: "))


if edat<18 or edat>40:
    print("No tens edat per competir")
elif edat>=18 and edat<=40 and classificaciò=="Si" or estat_físic=="Excel·lent":
    print("Pots participar a la competició")     
else:
    print("No pots participar")