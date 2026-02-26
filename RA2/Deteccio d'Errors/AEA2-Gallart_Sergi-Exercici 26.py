try:
    numero = float(input("Introdueix un número: ")) #Demanem a l'usuari que introdueixi un número i el convertim a decimal
    resultat = 10 / numero
    print(f"El resultat de 10 / {numero} és: {resultat}")
except ValueError:
    print("Error: Has introduït un valor no vàlid. Si us plau, introdueix un número.") #Text que es mostra si l'usuari introdueix un número o un caràcter no vàlid
except ZeroDivisionError:
    print("Error: No es pot dividir entre zero.")  #Error que mostra si l'usuari introdueix el número 0