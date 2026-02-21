Quantitat_diners=int(input("Cuants diners vols ingressar al compte "))
Quantitat_despresany=Quantitat_diners*0.04 +Quantitat_diners
Quantitat_despre2sanys=Quantitat_despresany*0.04 +Quantitat_despresany
Quantitat_despres3anys=Quantitat_despre2sanys*0.04 +Quantitat_despre2sanys
num_quantitat1any= round(Quantitat_despresany,2)
num_quantitat2any= round(Quantitat_despre2sanys,2)
num_quantitat3any= round(Quantitat_despres3anys,2)

print(f"Els teus diners desprès de un any seràn {num_quantitat1any} €")
print(f"Els teus diners desprès del segon any seràn {num_quantitat2any} €")
print(f"Els teus diners desprès del tercer any seràn {num_quantitat3any} €")