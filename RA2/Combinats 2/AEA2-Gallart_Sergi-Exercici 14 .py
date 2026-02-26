import random
num=random.randint(0,10)
semafor3=False
comptador=1
while not semafor3:
    intent=int(input("Introdueix el numero que la màquina està pensant: "))
    if intent==num:
        print(f"Has guanyat, el numero era {num}")
        semafor3=True
    elif comptador==3:
        semafor3=True
        print("Has perdut!")
    elif intent!=num:
        print("Torna a a intentar-ho ")
        comptador=comptador + 1