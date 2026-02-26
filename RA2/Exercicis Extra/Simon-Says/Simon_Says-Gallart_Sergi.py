import random
from os import system
import time

print("Benvingut al joc de Simon Says!")
print("L'ordinador mostrarà una seqüència de números entre l'1 i el 4.")
print("Els números iguals es mostraran amb un asterisc (*) per facilitar la identificació!")
print("Has de recordar la seqüència i repetir-la. Si falles, el joc s'acaba!")
print("Prem ENTER per començar.")
input()

# Variables inicials
secuencia = []
ronda = 0 # Comptador de rondes
jugador_encertant = True  # Semàfor per controlar el joc

while jugador_encertant:
    ronda += 1
    # Afegeix un nou número a la seqüència
    nou_numero = random.randint(1, 4)
    secuencia.append(nou_numero)
    
    # Neteja la pantalla
    system('cls')
    print(f"Ronda {ronda}: Recorda la seqüència!")

    # Mostra la seqüència al jugador, amb identificació de números iguals
    for i, numero in enumerate(secuencia):
        # Si el número és igual al número anterior, afegim un asterisc per ressaltar-lo
        if i > 0 and numero == secuencia[i - 1]:
            print(f"{numero}*")  # Cada número en una nova línia
        else:
            print(f"{numero}")  # Cada número en una nova línia
        time.sleep(1.5)  # Temps de visualització per cada número
        system('cls')
    
    # Demana al jugador que repeteixi la seqüència
    print("Ara és el teu torn. Escriu la seqüència, separada per espais:")
    resposta = input("Seqüència: ")

    # Compara la resposta amb la seqüència correcta (sense utilitzar strip ni split)
    resposta_entrada = resposta.split()  # Convertim la resposta en una llista
    resposta_correcta = True

    if len(resposta_entrada) != len(secuencia):  # Si la longitud no coincideix, és incorrecte
        resposta_correcta = False
    else:
        for i in range(len(secuencia)):  # Comprovar element per element
            if int(resposta_entrada[i]) != secuencia[i]:
                resposta_correcta = False

    if resposta_correcta:
        print("Correcte! Prepareu-vos per a la següent ronda.")
        time.sleep(1)
    else:
        print("Incorrecte! Has fallat.")
        print("La seqüència correcta era:")
        for num in secuencia:
            print(num)  # Mostrem la seqüència correcta número per número
        print(f"Has arribat a la ronda {ronda}.")
        jugador_encertant = False  # El semàfor s'apaga i el joc s'acaba

print("Gràcies per jugar!")
