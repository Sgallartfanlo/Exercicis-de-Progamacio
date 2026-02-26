from os import system
import time

# Definim el saldo inicial
saldo = 0

# Funció per ingressar diners
def ingres(cantidad):
    global saldo
    saldo += cantidad

# Funció per retirar diners
def retirada(cantidad):
    global saldo
    if saldo >= cantidad:
        saldo -= cantidad
    else:
        print("No pots retirar diners, el teu saldo és insuficient")

# Funció per mostrar el saldo
def mostrar_saldo():
    print(f"El saldo actual és: {saldo}€")
    time.sleep(5)
    system("cls")

# Funció per mostrar el menú
def menu():
    semafor = False
    while not semafor:
        print("1. Ingressar diners")
        print("2. Retirar diners")
        print("3. Mostrar saldo")
        print("4. Sortir")
        try:
            opcio = int(input("Què vols fer? "))
            if opcio == 1:
                cantidad = float(input("Quants diners vols ingressar? "))
                ingres(cantidad)
                print("Saldo actual: ", saldo, "€")
                time.sleep(4)
                system("cls")
            elif opcio == 2:
                cantidad = float(input("Quants diners vols retirar? "))
                retirada(cantidad)
                print("Saldo actual: ", saldo, "€")
                time.sleep(4)
                system("cls")
            elif opcio == 3:
                mostrar_saldo()
            elif opcio == 4:
                semafor = True
                print("Adeu!")
        except ValueError:
            print("Error: No has introduït un número vàlid")
            time.sleep(4)
            system("cls")
# Executem el menú
menu()