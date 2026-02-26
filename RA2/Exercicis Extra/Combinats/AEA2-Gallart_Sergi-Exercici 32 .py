numeros = [
   int(input("Introdueix el primer número: ")),
   int(input("Introdueix el segon número: ")),
   int(input("Introdueix el tercer número: "))
]
mes_gran = numeros[0]
mes_petit = numeros[0]
if numeros[1] > mes_gran:
   mes_gran = numeros[1]
if numeros[2] > mes_gran:
   mes_gran = numeros[2]

if numeros[1] < mes_petit:
   mes_petit = numeros[1]
if numeros[2] < mes_petit:
   mes_petit = numeros[2]
print(f"El número més gran és: {mes_gran}")
print(f"El número més petit és: {mes_petit}")