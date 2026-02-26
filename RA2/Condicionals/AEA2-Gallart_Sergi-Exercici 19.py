nota=float(input("Introdueix la nota que has tret: "))
# Classificació de la nota
if nota < 0 or nota > 10:
    print("La nota introduïda no és vàlida. Si us plau, introdueix un número entre 0 i 10.")
elif nota < 5:
    print("Classificació: Suspès")
elif nota < 7:
    print("Has aprovat per la mínima, posa't les piles")
elif nota < 9:
    print("Has aprovat amb un notable, pots fer una mica més.")
else:
    print("Has aprovat amb un Excel·lent, segueix així")