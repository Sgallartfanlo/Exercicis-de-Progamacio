edat=int(input("Introdueix la teva edat: "))
subscripciò=str(input("Estàs subcrit Sí o No: "))
premium=str(input("Tens compte premium Sí o No: "))


if edat>40 or subscripciò=="Si" and premium=="Si":
    print("Pots accedir al contingut")
else:
    print("No pots accedir")