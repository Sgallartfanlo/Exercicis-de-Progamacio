preu_barra = 3.49
descompte = 0.60


num_barres_avui = int(input("Introdueix el número de barres d'avui: "))
num_barres_ahir = int(input("Introdueix el número de barres d'ahir: "))


num_barres_vendes_avui = int(input("Introdueix el número de barres venudes d'avui: "))
num_barres_vendes_ahir = int(input("Introdueix el número de barres venudes d'ahir: "))


  
preu_total_avui = num_barres_vendes_avui * preu_barra
preu_total_ahir = num_barres_vendes_ahir * preu_barra * (1 - descompte)


preu_total = preu_total_avui + preu_total_ahir


print(f"El preu total de les barres venudes és {preu_total:.2f} euros.")
