edat=int(input("Introdueix la teva edat: "))
carnet=str(input("Tens Carnet de conduïr Sí o No: "))
alcohol=str(input("Vas sota els efectes de l'alcohol Sí o No: "))


if edat>=18 and carnet=="Si" and alcohol=="No":
    print("Pots conduïr")
else:
    print("No pots conduïr")
