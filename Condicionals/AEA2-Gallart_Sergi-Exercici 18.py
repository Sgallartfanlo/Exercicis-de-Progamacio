barra_pa=3.49
num_barres_avui=int(input("Introdueix el número de barres que tenim d' avui: "))
num_barres_ahir=int(input("Introdueix el número de barres que tenim d' ahir: "))
num_barres_client=int(input("Quantes barres vols? "))

preu_barres_total=num_barres_client * barra_pa 
descompte=preu_barres_total/100*60
preu_descompte=preu_barres_total-descompte
if num_barres_client>num_barres_avui:
    print("No ens queda estoc de  barres d'avui")
elif num_barres_client>num_barres_ahir:
    print("No ens queda estoc de barres d'ahir")
else:
    print(f"El preu de les {num_barres_client} barres d'avui és de {round(barra_pa*num_barres_client,2)} € ")
    print(f"El preu de les {num_barres_client} barres d'ahir és de {round(preu_descompte,2)} € ")