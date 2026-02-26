frase=str(input("Introdueix una frase: "))
lletra=str(input("Introdueix la lletra a cercar: "))
index = 0
comptador = 0
while index < len(frase):
   if frase[index] == lletra:
       comptador += 1
   index += 1
print(f"La lletra{lletra} apareix:", comptador, "vegades a la frase")