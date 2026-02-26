from random import *
num_min=int(input("Introdueix un número mínim: "))
num_max=int(input("Introdueix un número màxim: "))
if num_min>num_max or num_max<num_min:
    print("Error catastròfic, el màxim no pot ser més petit i viceversa i els números no poden ser iguals")
num_random=randint(num_min,num_max)
num_usuari=int(input("Introdueix el número que creus que la màquina està pensant: "))

if num_usuari>num_random:
    print("El número és més petit.")
elif num_usuari<num_random:
    print("El número és més gran.")
else:
    print("Has encertat el número")