import random

# Inicialització de les variables
semafor = False

# Demanem els límits mínim i màxim fins que siguin vàlids
while not semafor:
    num_min = int(input("Introdueix un número mínim: "))
    num_max = int(input("Introdueix un número màxim: "))
    
    if num_min > num_max:
        print("Error catastròfic: el màxim no pot ser més petit que el mínim.")
    elif num_max - num_min < 3:
        print("Error: ha d'haver almenys 3 números entre el mínim i el màxim.")
    else:
        semafor = True  # Els números són vàlids, canviem el semàfor a True


num_random = random.randint(num_min, num_max)
intents = 0
semafor_333 = False


while not semafor_333:
    num_usuari = int(input("Introdueix el número que creus que la màquina està pensant: "))
    intents += 1  
    if num_usuari > num_random:
        print("El número és més petit.")
        print(f"Portes {intents} intents")
    elif num_usuari < num_random:
        print("El número és més gran.")
        print(f"Portes {intents} intents")
    else:
        print(f"Has encertat el número amb {intents} intents!")
        semafor_333 = True  