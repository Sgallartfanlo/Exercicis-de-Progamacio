import time
import random

# Introducció del jugador i de l'enemic
nom = str(input("Digues el teu nom de guerra, per començar l'aventura: "))
enemic = str(input("Introdueix un nom per l'enemic: "))
bacteria = str(input("Introdueix un nom per a la bacteria: "))
print(f"Benvingut {nom}, prepara't que surts")
time.sleep(3)
print(f"Et trobes en una terra posseïda per un esser malvat anomenat {enemic} que ha desplegat una bacteria anomenada {bacteria}, que converteix a les persones en els seus súbdits")
time.sleep(3)
print(f"Un cop creus que t'has contaminat de {bacteria}...")
time.sleep(3)
print("De sobte surten uns bitxos de les clavegueres, que semblen unes tortugues.")
time.sleep(3)
print("Aquestes et subministren una mascareta i un mapa, i de sobte desapareixen.")
time.sleep(3)
print("Mires el mapa i veus que marca una ubicació, creus que és la sortida de la ciutat.")
time.sleep(3)
print("Però...")
time.sleep(3)
print("Et fixes que el mapa està en una altra llengua, sembla una llengua antiga.")
time.sleep(3)
print("Busques al teu mòbil i veus que la llengua és una llengua romana.")
time.sleep(3)
print(f"Gràcies al teu mòbil tradueixes el mapa i aquest conté la localització d'uns objectes per derrotar en {enemic}.")
time.sleep(3)
print("Un cop estàs a punt d'arribar a la localització...")
time.sleep(3)
print("Surt un jove d'aparença peculiar amb cabell groc i ulls blaus, amb un bastó extensible a l'esquena.")
time.sleep(3)
print("I et diu: En una d'aquestes dues coves trobaràs l'èxit, en canvi a l'altra trobaràs la teva perdició, que la sort t'acompanyi.")
time.sleep(3)

# Iniciem les variables
coves_encertades = 0
semafor = False
joc_acabat = False  # Nova variable per controlar si el joc ha acabat

# Col·lecció de textos ambientals per a les coves
descripcions_coves = [
    "La cova està plena de cristalls brillants que reflecteixen la llum.",
    "Sents un murmuri estrany que prové de les profunditats de la cova.",
    "L'aire és fresc i humit, i l'olor de terra humida et envolta.",
    "Veus ombres que es mouen a les parets de la cova, com si estiguessin vives.",
    "Un riu subterrani flueix lentament, creant un so relaxant.",
    "Les parets de la cova estan cobertes de molsa verda que brilla lleugerament.",
    "Sents el so de gotes d'aigua que cauen, creant un ritornell tranquil.",
]

# Començament del joc
while not joc_acabat:
    if not descripcions_coves:  # Si no hi ha més descripcions, reiniciem la llista
        descripcions_coves = [
            "La cova està plena de cristalls brillants que reflecteixen la llum.",
            "Sents un murmuri estrany que prové de les profunditats de la cova.",
            "L'aire és fresc i humit, i l'olor de terra humida et envolta.",
            "Veus ombres que es mouen a les parets de la cova, com si estiguessin vives.",
            "Un riu subterrani flueix lentament, creant un so relaxant.",
            "Les parets de la cova estan cobertes de molsa verda que brilla lleugerament.",
            "Sents el so de gotes d'aigua que cauen, creant un ritornell tranquil.",
        ]

    # Seleccionar una descripció aleatòria
    descripcio = random.choice(descripcions_coves)
    descripcions_coves.remove(descripcio)  # Eliminar la descripció seleccionada de la llista

    decisio = input(f"Escull amb saviesa {nom} quina cova esculls? (1 o 2 per entrar a la cova, 'Cap' per escapar): ")

    if decisio == "Cap":
        print("Has decidit fugir, la teva persona serà recordada per ser un maleït egoista i covard per només pensar en la teva persona, i de sobte surt un ésser humà darrer la pedra, i et mata d'un tir a la columna vertebral.")
        joc_acabat = True  # Canviar l'estat del joc a acabat
    else:
        print(f"Et trobes davant d'una cova. {descripcio}")  # Mostrar la descripció seleccionada

        if decisio == "1":
            print("Vas caminant per la cova número 1 i de sobte...")
            time.sleep(3)
            print("El terra es mou d'una manera poc peculiar, comença a sortir un fluïd de color rosa, i es va unint, formant una figura que sembla una persona, però de persona té poc, és un monstre?.")
            time.sleep(3)
            print("Un cop el monstre s'ha format al 100%, obre els ulls i... ")
            time.sleep(3)
            print("Et llença un raig que et converteix en xocolata i es comença a divertir com si fossis el seu amic, però de sobte...")
            time.sleep(3)
            print(f"Comença a llançar-te boles d'energia fins que desapareixes, en els teus últims sospirs et fixes que el monstre ha absorbit la teva energia, i ell se'n va a lluitar contra en {enemic}.")
            joc_acabat = True

        elif decisio == "2":
            print("Vas caminant per la cova número 2 i de sobte...")
            time.sleep(3)
            print("El terra comença a tremolar i de les esquerdes surt un cofre, i decideixes obrir-lo, del cofre surt... ")
            time.sleep(3)
            print("Et fixes que al fons, hi ha unes 7 esferes de color taronja amb cada una un nombre d'estrelles de l'1 al 7, i un paper que diu: ")
            time.sleep(3)
            print("Si al drac místic vols cridar, les set boles hauràs de juntar i el seu nom cridar.")
            time.sleep(3)
            print("Decideixes ajuntar totes les boles i cridar un nom que estava escrit al paper amb una lletra minúscula. De sobte, apareix un drac que et mira amb curiositat.")
            time.sleep(3)
            print("El drac et diu: 'Gràcies per alliberar-me! Ara et donaré poder per derrotar a l'enemic.'")
            time.sleep(3)
            coves_encertades += 1
            print(f"Has encertat! Coves encertades: {coves_encertades}")
            reinici = int(input("Vols tornar a jugar? 1-Si o 2-No Introdueix el número corresponent: "))
            if reinici == 1:
                semafor = False
                coves_encertades = 0  # Reiniciar el comptador de coves encertades
            elif reinici == 2:
                print("Has decidit no continuar, et trobarem a faltar")
                joc_acabat = True

        else:
            print("Decisió no vàlida, torna a decidir")
            semafor = False

# Final del joc
print(f"El joc ha acabat. Has encertat un total de {coves_encertades} coves.")