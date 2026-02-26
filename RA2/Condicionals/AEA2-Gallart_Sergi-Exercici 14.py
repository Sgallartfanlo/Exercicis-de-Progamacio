costat_1 = int(input("Introdueix el valor del primer costat: "))
costat_2 = int(input("Introdueix el valor del segon costat: "))
costat_3 = int(input("Introdueix el valor del tercer costat: "))

if costat_1 == costat_2 == costat_3:
    print("El triangle és equilàter.")
elif costat_1 == costat_2 or costat_1 == costat_3 or costat_2 == costat_3:
    print("Es un triangle isòsceles.")
else:
    print("Es un triangle escalè")