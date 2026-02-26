semafor1=False
resultat=0
llista_num=[]
while not semafor1:
    num=int(input("Introdueix un numero: "))
    if num>0:
        llista_num.append(num)
    elif num==0:
        semafor1=True
        print(llista_num)
    elif num<0:
        print("El numero no es vàlid")6