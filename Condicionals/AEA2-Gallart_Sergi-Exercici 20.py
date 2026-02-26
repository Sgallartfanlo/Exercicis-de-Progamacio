temperatura=int(input("Introdueix la temperatura actual: "))

if temperatura<=10:
    print("Fa fred")
elif temperatura>=30:
    print("Fa calor")
elif temperatura>10 and temperatura<30:
    print("Fa una temperatura moderada")