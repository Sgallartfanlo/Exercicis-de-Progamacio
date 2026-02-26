import random


# Generem un número aleatori entre 1 i 100
numero_secret = random.randint(1, 100)
intent = 0
encertat = False

# Iniciem el joc
print("Benvingut al joc d'endevinar el número!")
print("Has d'endevinar un número entre 1 i 100.")

# Bucle fins que l'usuari endevini el número
while not encertat:
    try:
        # Demanem a l'usuari un número i assegurem que sigui enter
        usuari_input = input("Introdueix el teu intent: ")


        # Comprovem si l'usuari introdueix un nombre enter
        numero_introduit = int(usuari_input)
       
        # Incrementem el nombre d'intents
        intent += 1


        # Comprovem si el número introduït és correcte
        if numero_introduit < numero_secret:
            print("El número secret és més gran. Intenta-ho de nou.")
        elif numero_introduit > numero_secret:
            print("El número secret és més petit. Intenta-ho de nou.")
        else:
            encertat = True
            print(f"Felicitats! Has endevinat el número {numero_secret} en {intent} intents.")


    except ValueError:
        # Si l'usuari no introdueix un número enter
        print("Error: Has de posar un número enter. Torna-ho a provar.")
