numeros = [
   int(input("Introdueix el primer número: ")),
   int(input("Introdueix el segon número: ")),
   int(input("Introdueix el tercer número: "))
]
if numeros[0] % 2 == 0:
   print(f"{numeros[0]} és parell.")
else:
   print(f"{numeros[0]} és senar.")

if numeros[1] % 2 == 0:
   print(f"{numeros[1]} és parell.")
else:
   print(f"{numeros[1]} és senar.")

if numeros[2] % 2 == 0:
   print(f"{numeros[2]} és parell.")
else:
   print(f"{numeros[2]} és senar.")