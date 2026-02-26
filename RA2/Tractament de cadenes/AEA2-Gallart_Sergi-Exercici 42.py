frase = str(input("Introdueix una frase: "))
paraules_frase = frase.split()
paraules_majus = []

for paraula in paraules_frase:
    paraules_majus.append(paraula.capitalize())

frase_majus = ' '.join(paraules_majus)
print(frase_majus)