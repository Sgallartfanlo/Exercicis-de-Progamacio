from os import system
import time

# Funció per ingressar diners
def ingres(saldo, quantitat):
    saldo += quantitat
    return saldo

# Funció per retirar diners
def retirada(saldo, quantitat):
    if saldo >= quantitat:
        saldo -= quantitat
    else:
        print("No pots retirar diners, el teu saldo és insuficient")
    return saldo

# Funció per mostrar el saldo
def mostrar_saldo(saldo):
    print(f"El saldo actual és: {saldo}€")
    time.sleep(5)
    system("cls")

# Funció per mostrar el menú
def menu():
    saldo = 0
    semafor = False
    while not semafor:
        print("1. Ingressar diners")
        print("2. Retirar diners")
        print("3. Mostrar saldo")
        print("4. Sortir")
        try:
            opcio = int(input("Què vols fer? "))
            if opcio == 1:
                quantitat = float(input("Quants diners vols ingressar? "))
                saldo = ingres(saldo, quantitat)
                print("Saldo actual: ", saldo, "€")
                time.sleep(4)
                system("cls")
            elif opcio == 2:
                quantitat = float(input("Quants diners vols retirar? "))
                saldo = retirada(saldo, quantitat)
                print("Saldo actual: ", saldo, "€")
                time.sleep(4)
                system("cls")
            elif opcio == 3:
                mostrar_saldo(saldo)
            elif opcio == 4:
                semafor = True
                print("Adeu!")
        except ValueError:
            print("Error: No has introduït un número vàlid")
            time.sleep(4)
            system("cls")
# Executem el menú
menu()