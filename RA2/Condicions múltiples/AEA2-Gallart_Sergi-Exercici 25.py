ingressos=int(input("Introdueix els teus ingressos: "))
deute=str(input("Tens algun deute Sí o No: "))
estalvis=int(input("Introdueix els teus estalvis "))


if ingressos>2000 and deute=="No" and estalvis>1000:
    print("Pots demananar un prèstec")
else:
    print("No el pots demanar")