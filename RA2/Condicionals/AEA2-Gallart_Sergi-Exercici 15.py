numero_1=int(input("Introdueix el primer número: "))
numero_2=int(input("Introdueix el segon número: "))

print("Tria quia operaciò desitja fer: ")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
opciò=int(input("Introdueix el número de la operciò que desitja realitzar: "))

if opciò==1:
    print(f"El resultat de la operaciò és {numero_1+numero_2}.")
elif opciò==2:
    print(f"El resultat de la operaciò és {numero_1-numero_2}.")
elif opciò==3:
    print(f"El resultat de la operaciò és {numero_1*numero_2}.")
else:
    print(f"El resultat de la operaciò és {numero_1/numero_2}.")