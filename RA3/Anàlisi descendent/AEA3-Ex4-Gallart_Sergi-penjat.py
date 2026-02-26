import random

def seleccionar_paraula():
    #Escull una paraula aleatòria d'una col·lecció.
    paraules = ["programar", "python", "joc", "penjat", "desenvolupament"]
    return random.choice(paraules)

def mostrar_estat(paraula, lletres_endevinades):
    #Mostra l'estat actual de la paraula amb les lletres endevinades.
    return ''.join([lletra if lletra in lletres_endevinades else '_' for lletra in paraula])

def validar_entrada(entrada, lletres_endevinades):
    #Valida l'entrada de l'usuari.
    if len(entrada) != 1 or not entrada.isalpha():
        return "Entrada no vàlida. Si us plau, introdueix una sola lletra."
    if entrada in lletres_endevinades:
        return "Ja has endevinat aquesta lletra."
    return None

def actualitzar_intents(entrada, paraula, intents):
    #Redueix el nombre d'intents si la lletra no és a la paraula.
    if entrada not in paraula:
        intents -= 1
        print(f"La lletra '{entrada}' no és a la paraula.")
    return intents

def comprovar_paraula_endevinada(paraula, lletres_endevinades):
    #Comprova si totes les lletres de la paraula han estat endevinades.
    return all(lletra in lletres_endevinades for lletra in paraula)

def joc_del_penjat():
    #Funció principal que executa el joc del penjat.
    paraula = seleccionar_paraula()
    lletres_endevinades = set()
    intents = 6
    print("Benvingut al joc del penjat!")
    while intents > 0:
        estat = mostrar_estat(paraula, lletres_endevinades)
        print(f"Paraula: {estat}")
        print(f"Intents restants: {intents}")

        entrada = input("Introdueix una lletra: ").lower()
        error = validar_entrada(entrada, lletres_endevinades)

        if error:
            print(error)
        else:
            lletres_endevinades.add(entrada)
            intents = actualitzar_intents(entrada, paraula, intents)

            if comprovar_paraula_endevinada(paraula, lletres_endevinades):
                print(f"Felicitats! Has endevinat la paraula: {paraula}")
                return

    print(f"Has perdut! La paraula era: {paraula}")

# Executar el joc
if __name__ == "__main__":
    joc_del_penjat()
