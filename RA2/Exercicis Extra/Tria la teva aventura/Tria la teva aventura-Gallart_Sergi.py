import random
from os import system
# Preguntes organitzades per categories
categories = {
    "Geografia": {
        "Quina és la capital de França?": ["a) Berlín", "b) Madrid", "c) París", "d) Roma"],
        "Quin és l'oceà més gran del món?": ["a) Atlàntic", "b) Índic", "c) Àrtic", "d) Pacífic"],
        "Com es diu el riu més famós d'egipte?":["a)Nil","b)Amazones","c)Mississipí","d)Tamesis"],
        "Quina és la capital de Suïsa?":["a)Zuric","b)Ginebra","c)Berna","d)Lausana"],
        "Quin és el desser més gran del món?":["a)Gobi","b)Sàhara","c)Antàrtida","d)Kalahari"],
        "Quin país té la major quantitat d'illes?":["a)Indonèsia","b)Suècia","c)Japó","d)Filipines"],
        "A quin continent es troba la serralada de l'Himàlaia?":["a)Àfrica","b)Àsia","c)Europa","d)Amèrica del Sud"],
        "Quants països formen part de la Unió Europea (UE) actualment?":["a)25","b)27","c)28","d)30"],
        "A quin país pertany l'arxipèlag de les Galápagos?":["a)Perú","b)Xile","c)Equador","d)Colòmbia"],
        "Quin és el país més gran del món en superfície?":["a)Canadà","b)Rússia","c)Xina","d)Estats Units"]
    },
    "Ciència": {
        "Què és l'ADN?": ["a) Àcid desoxiribonucleic", "b) Àcid ribonucleic", "c) Una proteïna", "d) Un carbohidrat"],
        "Quants planetes hi ha al sistema solar?": ["a) 7", "b) 8", "c) 9", "d) 10"],
        "Quin tipus de partícula té càrrega positiva?":["a)Electrò","b)Protó","c)Neutrí","Neutró"],
        "Quin és el planeta més gran del sistema solar?":["a)Júpiter","b)Saturn","c)Neptú","d)Urà"],
        "Quin és l'element químic amb el símbol O?":["a)Oxigen","b)Or","c)Osmí","d)Òxid"],
        "Quina unitat s'utilitza per mesurar la força?":["a)Joule","b)Newton","c)Watt","d)Pascal"],
        "Quina part de la cèl·lula conté el material genètic?":["a)Citoplasma","b)NNucli","c)Membrana cel·lular","d)Mitocondri"],
        "Quina és la velocitat de la llum en el buit?":["a)150.000 km/s","b)300.000 km/s","c)450.000 km/s","d)600.000 km/s"],
        "Quin és el pH d'una solució neutra?":["a)0","b)7","c)10","d)14"],
        "Com es diu el procés pel qual les plantes converteixen la llum solar en energia?":["a)Respiració","b)Fermentació","c)Fotosíntesi","d)Transpiració"]

    },
    "Literatura": {
        "Qui és l'autor de El Quixot":["a)Lope de Vega","b)Miguel de Cervantes","c)Garcilaso de la Vega","d)Francisco de Quevedo"],
        "Quina obra va escriure Willian Shakespeare":["a)La casa de bernarda Alba","b)Romeu i Julieta","c)El Decameró","d)La divina"],
        "Quin és el nom del protagonista de La metamorfosi de Franz Kafka?":["a)Gregor Samsa","b)Raskólnikov","c)Leopold Bloom","d)Santiago Nasar"],
        "Quin escriptor català és l'autor de Tirant lo Blanc?":["a)Ramon Llull","b)Joanot Martorell","c)Ausiàs March","d)Jacit Verdaguer"],
        "Qui va escriure 'Cents anys de solitud'?": ["a) Julio Cortázar", "b) Gabriel García Márquez", "c) Mario Vargas Llosa", "d) Jorge Luis Borges"],
        "Quina obra comença amb la frase:""Tots els animals són iguals, però alguns són més iguals que els altres?":["a)1984","b)Un món feliç","c)Rebel·lió a la granja","d)Fahrenheit 451"],
        "Quin gènere literari es caracteritza per l'ús de mites i llegendes per explicar fenòmens naturals?":["a)Novel·la","b)Poesia èpica","c)Mitologia","d)Assaig"],
        "Quin autor va escriure La casa de Bernarda Alba?":["a)Federico García Lorca","b)Antonio Machado","c)Juan Ramón Jiménez","d)Rubén Darío"],
        "Quina obra és considerada el poema èpic més antic conservat?":["a)La Ilíada","b)El poema de Gilgamesh","c)L’Odissea","d)Beowulf"],
        "Quin poeta és l'autor de Cant espiritual?":["a)Joan Maragall","b)Ausiàs March","c)Miquel Martí i Pol","d)Salvador Espriu"]
    },
    "Esports": {
    "Quin futbolista té més pilotes d'or?": ["a)Cristiano Ronaldo", "b) Ronaldo Nazario", "c) Leo Messi", "d) Maradona"],
    "Quin atleta té el rècord dels 100 metres llisos?": ["a)Usain Bolt","b)Noah Lyles","c)Kishane Thompson","c)Filippo Tortu"],
    "Quin és l'equip de la NBA amb més títols?": ["a)Lakers","b)Chicago Bulls","c)Toronto Raptors","d)Boston Celtics"],
    "Quant dura una marató?":["a)42Km","b)33Km","c)52Km","d)48Km"],
    "Quin és l'esport més popular a la Índia?":["a)Futbol","b)Bàsquet","c)Criquet","d)Judo"],
    "Quin és l'esport més practicat del mon?":["a)Futbol","b)Natació","c)Bàsquet","d)Atletisme"],
    "Quin dorsal va portar Carles Puyol en el FCBarcelona la major part de la seva carrera?":["a)24","b)30","c)5","d)6"],
    "De quin país es nascut Erling Braut Haaland?":["a)Noruega","b)Regne Unit","c)Suecia","d)Finlandia"],
    "Quina peça d'escacs pot fer un moviment en forma de L?":["a)El cavall","b)L'alfil","c)El peó","d)La torre"],
    "Quants minuts totals té de durada un partit de fútbol?":["a)60min","b)120min","c)90min","d)45min"]
    }
}
#Respostes correctes de les preguntes
respostes_correctes = {
    "Geografia": ["c", "d","a","c","c","b","b","b","c","b"],
    "Ciència": ["a", "b","b","a","a","b","b","b","b","c"],
    "Literatura": ["b","b","a","b","a","c","c","a","b","a"],
    "Esports": ["c","a","d","a","c","b","c","b","a","c"],
}

# Escollir categoria
print("Escull una categoria:")
for categoria in categories:
    print(f"- {categoria}")

categoria_escollida = input("La teva elecció: ")

if categoria_escollida not in categories:
    print("Categoria no vàlida. S'acabarà el joc.")
else:
    preguntes = categories[categoria_escollida]
    respostes_correctes_categoria = respostes_correctes[categoria_escollida]
    punctuacio = 0
    numero_de_preguntes = len(preguntes)

    print(f"Benvingut al joc de Trivia de la categoria '{categoria_escollida}'!")
    print("Respon les següents preguntes amb la lletra corresponent (a, b, c o d):")

    # Comptador per les preguntes
    i = 0
    for pregunta in preguntes:
        print(f"Pregunta {i + 1}: {pregunta}")
        for opcio in preguntes[pregunta]:
            print(opcio)

        resposta = input("La teva resposta: ")

        if resposta == respostes_correctes_categoria[i]:
            print("¡Correcte!")
            punctuacio += 1
        else:
            print("Incorrecte.")
        i += 1
    print(f"\nLa teva puntuació final és: {punctuacio} de {numero_de_preguntes}")