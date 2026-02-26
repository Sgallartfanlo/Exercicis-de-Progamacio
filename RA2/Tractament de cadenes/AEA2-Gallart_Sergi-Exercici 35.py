# Demanem a l'usuari que introdueixi una frase
frase = str(input("Introdueix una frase: "))
# Demanem a l'usuari que introdueixi una paraula
paraula = str(input("Introdueix una paraula: "))
#Comprovem si la paraula està dins de la frase inserida per l'usuari, si està li mostrem la posiciò
if paraula in frase:
    print(f"La paraula '{paraula}' està dins de la frase i éstà en la posiciò numero:",frase.find(paraula))
else:
    print(f"La paraula '{paraula}' NO està dins de la frase.")