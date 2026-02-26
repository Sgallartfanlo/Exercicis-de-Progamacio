numero_1=int(input("Introdueix el primer número: "))
numero_2=int(input("Introdueix el segon número: "))

if numero_1% 10==0 or numero_2% 10==0:
    print("Com a mínim un dels dos números és divisible entre 10.")
else:
    print("Cap dels números és divisible entre 10.")