semafor1=False
resultat=0
comptador=0
while not semafor1:
    num=int(input("Introdueix un numero: "))
    resultat=resultat+num
    comptador=comptador+1
    if comptador==5:
        semafor1=True
        print(f"La suma de tots els numeros és {resultat}")