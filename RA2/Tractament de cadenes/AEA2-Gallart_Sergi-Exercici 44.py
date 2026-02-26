paraula=str(input("Introdueix una paraula: "))

if paraula==paraula[::-1]:
    print("La paraula és palíndrom")
else:
    print("La paraula no és palíndrom")