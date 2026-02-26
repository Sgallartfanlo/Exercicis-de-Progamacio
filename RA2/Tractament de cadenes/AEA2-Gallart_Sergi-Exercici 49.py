# Demanar una frase a l'usuari
frase_input = input("Introdueix una frase: ")
# Inicialitzar la nova frase
nova_frase = ""
# Definim les vocals
vocals = "aeiouAEIOUàèéíòóúÀÈÉíÒÓÚ"

# Recórrer cada caracter de la frase
for caracter in frase_input:
    if caracter in vocals:
        nova_frase += caracter.upper()  # Substituir la vocal per la seva versió en majúscula
    else:
        nova_frase += caracter  # Mantenir el caracter original

# Mostrar la frase modificada
print("Frase modificada:", nova_frase)
