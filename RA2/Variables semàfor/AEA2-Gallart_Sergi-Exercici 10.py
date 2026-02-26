import random
numero_correcte=False
num_endevinar=random.randint(1,10)

while not numero_correcte:
    num_usuari=int(input("Quin número creus que ha pensat la màquina? "))
    if num_usuari==num_endevinar:
        numero_correcte=True
        print("Has enertat el número!")
    else:
        print("No has encertat, torna a provar.")