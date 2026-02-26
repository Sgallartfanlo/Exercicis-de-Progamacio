
diners=str(input("Disposes de la quantitat de diners per a comprar l'objecte? Sí o No: "))
descompte=str(input("L'objecte té descompte o alguna oferta? Sí o No: "))
targeta_fidelitat=str(input("Tens una targeta de fidelitat? Sí o No: "))


if diners=="Si" and descompte=="Si" or targeta_fidelitat=="Si":
    print("Pots comprar l'objecte")
else:
    print("No el pots comprar.")