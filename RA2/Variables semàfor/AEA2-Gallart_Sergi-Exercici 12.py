semafor=False
llista=[1,23,42,59,66,77,33,2,84]
comptador=0
while not semafor:
    num=llista[comptador]
    if num%2==0:
        print(f"El numero {num} es parell")
        semafor=True
    else:
        comptador=comptador+1
        semafor=False