radi=int(input("Introdueix el radi de la circumferència: "))
PI=3.14

print("Quin càlcul vols realitzar sobre la circumferència?")
print("1: Longitud")
print("2: Àrea")
num_càlcul=int(input("Introdueix el número corresponent del càlcul: "))

if num_càlcul==1:
    print(f"La longitud de la circumferència és de {radi*2*PI} ")
elif num_càlcul==2:
    print(f"L'àrea de la circumferèencia és de {PI*radi**2} ")