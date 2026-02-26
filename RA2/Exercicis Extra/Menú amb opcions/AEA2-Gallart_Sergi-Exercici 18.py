numero_1=int(input("Introdueix el primer número: "))
numero_2=int(input("Introdueix el segon número: "))
semafor_1=False
print("Tria quia operaciò desitja fer: ")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("-1 Per sortir del programa")
while not semafor_1:
    opciò=int(input("Introdueix el número de la operciò que desitja realitzar: "))
    if opciò==1:
        print(f"El resultat de la operaciò és {numero_1+numero_2}.")
    elif opciò==2:
        print(f"El resultat de la operaciò és {numero_1-numero_2}.")
    elif opciò==3:
        print(f"El resultat de la operaciò és {numero_1*numero_2}.")
    elif opciò==-1:
        semafor_1=True
    else:
        print(f"El resultat de la operaciò és {numero_1/numero_2}.")