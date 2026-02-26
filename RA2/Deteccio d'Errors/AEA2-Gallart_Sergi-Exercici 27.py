# Llista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Variable per a la suma
suma = 0
# Erroni: Afegim tots els números, no només els parells
for num in numeros:
    suma += num  # Error lògic: s'estan sumant tots els números, no només els parells
print(f"La suma de tots els números és: {suma}")