print("Benvingut al restaurant Medditerrànea")

print("Tens els segünts plats a la carta:")
print("1.Pizza")
print("2.Hamburguesa")
print("3.Amanida")
print("4.Sopa")
num_plat=int(input("Tria un plat i escull el seu número: "))

if num_plat==1:
    print("Has escollit pizza")
elif num_plat==2:
    print("Has escollit Hamburguesa")
elif num_plat==3:
    print("Has escollit Amanida")
elif num_plat==4:
    print("Has escollit Sopa")
else:
    print("No tenim aquest plat, disculpa les molesties")