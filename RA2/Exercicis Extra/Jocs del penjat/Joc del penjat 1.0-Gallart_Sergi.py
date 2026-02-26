import random

# Col·lecció de paraules
paraules = ["programar", "python", "joc", "penjat", "desenvolupament"]

# Escollir una paraula aleatòriament
paraula = random.choice(paraules)
lletres_endevinades = set()
intents = 6  # Nombre d'intents disponibles

print("Benvingut al joc del penjat!")

while intents > 0:
    # Mostrar l'estat actual de la paraula
    estat = ''.join([lletra if lletra in lletres_endevinades else '_' for lletra in paraula])
    print(f"Paraula: {estat}")
    print(f"Intents restants: {intents}")
    
    entrada = input("Introdueix una lletra: ").lower()  # Convertim a minúscula directament

    # Validar l'entrada
    if len(entrada) != 1 or not entrada.isalpha():
        print("Entrada no vàlida. Si us plau, introdueix una sola lletra.")
        

    if entrada in lletres_endevinades:
        print("Ja has endevinat aquesta lletra.")
    else:
        lletres_endevinades.add(entrada)

        if entrada not in paraula:
            intents -= 1
            print(f"La lletra '{entrada}' no és a la paraula.")
        
    # Comprovar si s'ha endevinat la paraula
    paraula_endevinada = True
    for lletra in paraula:
        if lletra not in lletres_endevinades:
            paraula_endevinada = False
            # No fem break, continuem comprovant totes les lletres

    if paraula_endevinada:
        print(f"Felicitats! Has endevinat la paraula: {paraula}")
        intents = 0  # Acabem el joc establint intents a 0

# Si s'acaben els intents
if intents == 0 and not paraula_endevinada:
    print(f"Has perdut! La paraula era: {paraula}")