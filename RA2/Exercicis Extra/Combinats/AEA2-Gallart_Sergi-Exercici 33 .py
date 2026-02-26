# Demanem a l'usuari que introdueixi tres elements, que poden ser números o text.
element1 = eval(input("Introdueix el primer element (pot ser número o text(Si és text amb cometes)): "))
element2 = eval(input("Introdueix el segon element (pot ser número o text (Si és text amb cometes)): "))
element3 = eval(input("Introdueix el tercer element (pot ser número o text(Si és text amb cometes)): "))

# Creem una llista amb els tres elements introduïts.
elements = [element1, element2, element3]

# Comprovem el tipus del primer element i imprimim un missatge corresponent.
if type(elements[0]) == int:
   print(f"'{elements[0]}' és un enter.")
elif type(elements[0]) == float:
   print(f"'{elements[0]}' és un nombre decimal.")
elif type(elements[0]) == str:
   print(f"'{elements[0]}' és una cadena de text.")
elif type(elements[0]) == bool:
   print(f"'{elements[0]}' és un valor booleà.")
else:
   print(f"'{elements[0]}' és d'un altre tipus.")

# Comprovem el tipus del segon element i imprimim un missatge corresponent.
if type(elements[1]) == int:
   print(f"'{elements[1]}' és un enter.")
elif type(elements[1]) == float:
   print(f"'{elements[1]}' és un nombre decimal.")
elif type(elements[1]) == str:
   print(f"'{elements[1]}' és una cadena de text.")
elif type(elements[1]) == bool:
   print(f"'{elements[1]}' és un valor booleà.")
else:
   print(f"'{elements[1]}' és d'un altre tipus.")

# Comprovem el tipus del tercer element i imprimim un missatge corresponent.
if type(elements[2]) == int:
   print(f"'{elements[2]}' és un enter.")
elif type(elements[2]) == float:
   print(f"'{elements[2]}' és un nombre decimal.")
elif type(elements[2]) == str:
   print(f"'{elements[2]}' és una cadena de text.")
elif type(elements[2]) == bool:
   print(f"'{elements[2]}' és un valor booleà.")
else:
   print(f"'{elements[2]}' és d'un altre tipus.")