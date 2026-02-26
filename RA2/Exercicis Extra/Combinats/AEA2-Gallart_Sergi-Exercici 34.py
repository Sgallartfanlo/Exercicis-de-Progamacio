clients = {
   "Joan": 17,
   "Maria": 70,
   "Pere": 45
}
for nom, edat in clients.items():
   if edat < 18:
       descompte = 10
       print(f"{nom}, amb {edat} anys, té un descompte del {descompte}%")
   elif edat > 65:
       descompte = 20
       print(f"{nom}, amb {edat} anys, té un descompte del {descompte}%")
   else:
       print(f"{nom}, amb {edat} anys, no té descompte.")