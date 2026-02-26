paragraf = input("Introdueix un paràgraf: ")
frases = paragraf.split('.')

# Mostrar les frases resultants
for i, frase in enumerate(frases):
    frase = frase.strip()  # Eliminar espais en blanc al principi i al final
    if frase:  # Comprovar que la frase no estigui buida
        print(f"Frase {i + 1}: {frase}")