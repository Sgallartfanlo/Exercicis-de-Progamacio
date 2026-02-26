# Demanem a l'usuari que introdueixi dos números
try:
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    
    # Intentem realitzar una divisió
    result = num1 / num2
    print(f"El resultat de la divisió és: {result}")
    
    # Intentem accedir a un element d'una llista
    llista = [1, 2, 3]
    index = int(input("Introdueix un índex per accedir a la llista (0-2): "))
    print(f"L'element a l'índex {index} és: {llista[index]}")

except ValueError:
    print("Error: Has de introduir un número enter. Intenta-ho de nou.")
except ZeroDivisionError:
    print("Error: No es pot dividir per zero.")
except IndexError:
    print("Error: L'índex que has introduït està fora de l'abast de la llista.")
except Exception as e:
    print(f"S'ha produït un error inesperat: {e}")
else:
    print("Totes les operacions s'han realitzat correctament.")
finally:
    print("Aquest missatge es mostrarà independentment d'errors.")