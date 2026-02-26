energia=int(input("Introdueix la energia que tens "))
vida=int(input("Introdueix la vida que tens: "))
poder_especial=str(input("Disposes d'un poder especial Sí o No: "))


if energia>=0 and vida>=0 or poder_especial=="Si":
    print("Pots continuar jugant")
else:
    print("No pots continuar")