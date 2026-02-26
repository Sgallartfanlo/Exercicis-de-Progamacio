edat=int(input("Introdueix la teva edat "))
llista_negra=str(input("Estàs en una llista negra? Sí o No "))
invitació=str(input("Tens una invitació? Sí o No: "))


if edat>18 and llista_negra=="No" and invitació=="Si":
    print("Pots accedir a l'event")
else:
    print("No pots accedir")