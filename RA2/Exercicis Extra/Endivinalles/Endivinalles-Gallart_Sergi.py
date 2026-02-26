import random

#Lista amb les endivinalles i les sever respostes
endivinalles=[
    {"pregunta":"Mig groga i mig negra, vaig de flor en flor; si molt em molestes et clavo un fibló.","resposta": "abella"},
    {"pregunta":"Una pedra que camina sense ser pedra; té quatre cames i no és ovella, pon ous i no és gallina.","resposta": "tortuga"},
    {"pregunta":"Una caixa blanqueta com la calç, tots la saben obrir, però ningú la sap tancar.","resposta": "ou"},
    {"pregunta":"Quan em portes ben cordat soc bo i la teva aparença té un bon to. Qui soc?","resposta": "botó"},
    {"pregunta":"Blanca per dins, verda per fora. Si no saps, espera. Què és?","resposta": "pera"},
    {"pregunta":"Dues pinces té, cap enrere fa camí, de mar o de riu en l’aigua viu.","resposta": "cranc"},
    {"pregunta":"Alta com un pal, cap a dalt i només menja fulles que estan damunt. Què és?","resposta": "girafa"},
    {"pregunta":"Soc en blanc i negre, però no soc una tele vella, soc de fet un animal, que també serveixo perquè creuis la vorera.","resposta": "zebra"},
    {"pregunta":"Volo de nit, dormo de dia i mai no em veuràs plomes en la meva vida.","resposta": "ratpenat"},
]

semafor=True
while semafor:
    pregunta=random.choice(endivinalles)
    print(pregunta["pregunta"])
    resposta_usuari=str(input("Que creus què és?: ")).lower()
    if resposta_usuari==pregunta["resposta"]:
        print("La resposta és correcta, Segueix així.")
    else:
        print(f"La resposta és incorrecta, torna a intentar, la resposta correcta era:",pregunta["resposta"])
        semafor=False