edat=int(input("Escriu la teva edat: "))
sou=int(input("Introdueix el teu sou: "))
ciutat=str(input("Introdueix la ciutat on vius: "))
augment=sou/100*10

if edat<18:
    print(f"El teu sou duplicat és de {sou*2}€")
elif edat>18 and ciutat=="Barcelona" or "barcelona":
    print(f"El teu sou amb el augment del 10% es queda a {augment+sou}€ ")