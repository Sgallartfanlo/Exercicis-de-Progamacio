paraules=str(input("Introdueix una llista de paraules separades per comes: "))
paraules_separades=paraules.split(",")
print("Els elements introduïts són:")
for paraules in paraules_separades:
    print(paraules)