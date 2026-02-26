# Inicialitzem una variable per controlar si l'entrada és vàlida
entrada_valida = False
# Continuem demanant un número fins que l'usuari introdueixi un número enter vàlid
while not entrada_valida:
    try:
        # Sol·licitem a l'usuari que introdueixi un número enter
        num = int(input("Introdueix un número enter: "))
       
        # Si arribem aquí, significa que l'usuari ha introduït un número enter vàlid
        entrada_valida = True
       
    except ValueError:
        # Si es produeix un error (l'entrada no és un número enter), informem a l'usuari
        print("No has introduït un número enter, torna a provar-ho.")
       
# Informem a l'usuari que ha introduït el número correctament
print(f"Has introduït el número {num} correctament!")