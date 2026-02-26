semafor1=False
resultat=0
while not semafor1:
    num=int(input("Introdueix un numero: "))
    if num == -1:
        print(f"La suma de tots els numeros és {resultat}")
        semafor1=True
    elif num != -1:
        resultat=resultat+num
        print("El numero no serveix per sortir")