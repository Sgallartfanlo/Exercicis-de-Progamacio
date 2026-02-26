# Sol·licitar al usuari que introdueixi un correu electrònic
correu = input("Introdueix un correu electrònic: ")

# Comprovar si el correu té un format bàsic vàlid amb '@'
if "@" in correu:
    # Dividir el correu en dues parts: la part abans de '@' (local) i la part després (domini)
    local, domini = correu.split("@")
    # Si la part local és massa curta, no s'aplica la censura
    if len(local) > 2:
        # Mostrar només el primer i últim caràcter de la part local, amb asteriscs al mig
        local_censurat = f"{local[0]}{'*' * (len(local) - 2)}{local[-1]}"
    else:
        # Si és massa curta, es deixa tal qual
        local_censurat = local
    # Concatenar la part censurada amb el domini
    correu_censurat = f"{local_censurat}@{domini}"
    print(f"El correu censurat és: {correu_censurat}")
else:
    print("El format del correu no és vàlid.")
