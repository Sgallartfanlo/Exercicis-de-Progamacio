num=int(input("Introdueix un número: "))
while num%2==1:
    print("El numero no es parell")
    num=int(input("Introdueix un número: "))
    if num%2==0:
        print("El número es parell")