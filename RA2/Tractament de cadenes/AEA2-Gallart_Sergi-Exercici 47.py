frase=str(input("Introdueix una frase: "))
paraula=str(input("Introdueix la paraula a reemplaçar: "))
frase_modificada = frase.replace(paraula, '*' * len(paraula))
print("Frase Modificada:",frase_modificada)