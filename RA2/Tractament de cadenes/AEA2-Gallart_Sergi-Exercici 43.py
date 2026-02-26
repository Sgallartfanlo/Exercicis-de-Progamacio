# Demanem a l'usuari que introdueixi una frase
frase = input("Introdueix una frase: ")

# Inicialitzem una nova cadena buida per guardar la frase sense vocals
nova_frase = ""

# Definim les vocals
vocals = "aeiouAEIOUàèéíòóúÀÈÉíÒÓÚ"

# Utilitzem un bucle per recórrer cada caràcter de la frase
for caracter in frase:
    if caracter not in vocals:
        nova_frase += caracter

# Mostrem la nova frase sense vocals
print("Frase sense vocals:", nova_frase)