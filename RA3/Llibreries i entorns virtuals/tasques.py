import datetime
from termcolor import colored
from os import system
import time

def afegir_tasca(tasques, nom, data_limit):
    # Afegeix una nova tasca a la llista de tasques
    tasques.append({"nom": nom, "data_limit": data_limit})
    print(f"Tasca '{nom}' afegida amb èxit amb data límit {data_limit}.")
    time.sleep(3)  # Espera 3 segons
    system('cls')  # Neteja la pantalla

def mostrar_tasques(tasques):
    # Mostra totes les tasques amb el seu estat
    avui = datetime.date.today()
    for tasca in tasques:
        dies_restants = (tasca["data_limit"] - avui).days
        if dies_restants < 0:
            print(colored(f"[RETARD] Tasca: {tasca['nom']} - Data límit: {tasca['data_limit']} - {abs(dies_restants)} dies de retard!", "red"))
        elif dies_restants == 0:
            print(colored(f"[URGENT] Tasca: {tasca['nom']} - Data límit: {tasca['data_limit']} - Avui és el dia límit!", "yellow"))
        else:
            print(f"[PENDENT] Tasca: {tasca['nom']} - Data límit: {tasca['data_limit']} - Queden {dies_restants} dies.")

def eliminar_tasca(tasques, nom):
    # Elimina una tasca de la llista si existeix
    tasca_existeix = any(tasca["nom"] == nom for tasca in tasques)
    if not tasca_existeix:
        print(f"Error: La tasca '{nom}' no existeix.")
        time.sleep(2)
        system("cls")
        return
    tasques[:] = [tasca for tasca in tasques if tasca["nom"] != nom]
    print(f"Tasca '{nom}' eliminada.")
    print("Tasca eliminada amb èxit!")
    time.sleep(3)  # Espera 3 segons
    system('cls')  # Neteja la pantalla

def main():
    print(colored("Benvingut al Gestor de Tasques", "green"))
    time.sleep(3)  # Espera 3 segons
    system("cls")  # Neteja la pantalla
    print(colored("Carregant el gestor...", "green"))
    time.sleep(4)  # Espera 4 segons
    system("cls")  # Neteja la pantalla
    print(colored("Carrega Completa, ja pots gestionar les teves tasques!", "green"))
    time.sleep(2)  # Espera 2 segons
    system("cls")  # Neteja la pantalla
    tasques = []  # Inicialitza la llista de tasques
    opcio = ""
    while opcio != "4":
        # Mostra el menú d'opcions
        print("1. Afegir tasca")
        print("2. Mostrar tasques")
        print("3. Eliminar tasca")
        print("4. Sortir")
        opcio = input("Tria una opció: ")
        if opcio == "1":
            # Afegeix una nova tasca
            nom = input("Nom de la tasca: ")
            data_str = input("Data límit (DD/MM/YYYY): ")
            try:
                data_limit = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
                afegir_tasca(tasques, nom, data_limit)
            except ValueError:
                print("Data no vàlida. Torna-ho a intentar.")
        elif opcio == "2":
            # Mostra totes les tasques
            mostrar_tasques(tasques)
            time.sleep(10)  # Espera 10 segons
            system("cls")  # Neteja la pantalla
        elif opcio == "3":
            # Mostra les tasques actuals i elimina la tasca seleccionada
            print("Tasques actuals:")
            mostrar_tasques(tasques)
            nom = input("Nom de la tasca a eliminar: ")
            eliminar_tasca(tasques, nom)
        elif opcio != "4":
            # Opció no vàlida
            system("cls")  # Neteja la pantalla
            print("Opció no vàlida. Torna-ho a intentar.")