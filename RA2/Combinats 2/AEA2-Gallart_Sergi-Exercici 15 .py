semafor4=False
llista_paraules=[]
while not semafor4:
    paraula=str(input("Introdueix una paraula: "))
    if paraula=="stop":
        print(llista_paraules)
        semafor4=True
    elif len(paraula)>4:
        llista_paraules.append(paraula)