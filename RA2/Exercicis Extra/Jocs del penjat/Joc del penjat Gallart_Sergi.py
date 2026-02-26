paraula = ["g", "r", "o", "c",]
lletra = input("Introdueix una lletra en minúscula: ")

if lletra in paraula:
   index = paraula.index(lletra)
   print(f"Felicitats! La lletra '{lletra}' apareix a la posició {index + 1} de la paraula.")
else:
   
   print("La lletra no està a la paraula. Has perdut")
   print("""
   =======
     |   |
     O   |
    -|-  |
     |   |
    / \\  |
         |
   =======
   """)