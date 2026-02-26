# AEA3 - Exercici 1
try:
    a=int(input("Introdueix un número: ")) #Demanem dos números a l'usuari
except ValueError:
    print("No has introduit un número")
    a=int(input("Introdueix un número: "))
try:
    b=int(input("Introdueix un altre número: "))
except ValueError:
    print("No has introduit un número: ")
    b=int(input("Introdueix un altre número: "))

def suma(a,b):  #Definim les operacions
    return a+b
def resta(a,b):
    return a-b
def multiplicacio(a,b):
    return a*b
def divisio(a,b):
    if b==0:
        print("No es pot dividir per 0")
        return a/b
    else:
        return a/b

def menu():     #Definim el menú
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    opcio=int(input("Escull una opció: "))
    if opcio<1 or opcio>4:
        print("Opció incorrecta")
    if opcio==1:
        print(f"El resultat de la suma és:",suma(a,b))
    elif opcio==2:
        print(f"El resultat de la resta és:",resta(a,b))
    elif opcio==3:
        print(f"El resultat de la multiplicació és:",multiplicacio(a,b))
    elif opcio==4:
        print(f"El resultat de la divisió és:",divisio(a,b))
menu() #Cridem la funció menu