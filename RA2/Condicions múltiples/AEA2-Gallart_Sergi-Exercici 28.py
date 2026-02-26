edat=int(input("Introdueix la teva edat: "))
puntuaciò=int(input("Introdueix la puntuaciò que tens: "))
descualificaciò=str(input("Estas descualificat? Sí o No: "))


if edat>14 and puntuaciò>80 and descualificaciò=="No":
    print("Pots participar a la competició")
else:
    print("No pots participar")