num=int(input("Introdueix un número: "))
descompte=num/100*10
descompte_5=num/100*5

if num>5000:
    print(f"El número amb un 5% de descompte és de {num-descompte_5} ")
else:
    print(f"El número amb un 10% de descompte és de {num-descompte}")
