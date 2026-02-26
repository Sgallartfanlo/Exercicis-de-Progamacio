import random
puntuacio = 0
semafor_33 = False
num_tirada=0
while puntuacio < 20 and not semafor_33:
    llançament = random.randint(1, 6)
    num_tirada=num_tirada+1
    print(f"Has llançat un {llançament} en la tirada {num_tirada}")
    if llançament == 1:
        semafor_33 = True
    else:
        puntuacio += llançament
        print(f"Puntuació acumulada: {puntuacio}")
if semafor_33:
    print(f"Has perdut! El joc ha acabat en la tirada {num_tirada} amb una puntuaciò de {puntuacio}.")
else:
    print(f"Has guanyat amb {puntuacio} punts! Felicitats! ")