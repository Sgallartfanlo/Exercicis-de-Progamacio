# Demanar una frase a l'usuari
frase = input("Introdueix una frase: ")
nova_frase = ""

# Recórrer cada caràcter de la frase
for caracter in frase:
    # Comprovar si el caràcter és una vocal
    if caracter in "aeiou":
        nova_frase += caracter.upper()  # Substituir per la vocal en majúscula
    else:
        nova_frase += caracter  # Mantenir el caràcter original

# Imprimir la frase modificada
print("Frase modificada:", nova_frase)