pallassos=112
nines=75
n_pallassos=int(input("Escriu el numero de pallasos que van al paquet "))
n_nines=int(input("Escriu el numero de nines que van al paquet "))
p_pallassos= pallassos*n_pallassos
p_nines= nines*n_nines
pes_total= p_pallassos + p_nines
print(f"En el paquet hi han {n_pallassos} pallassos i aquests pesen un total de {p_pallassos} g també hi han {n_nines} nines i aquestes pesen en total {p_nines} g")
print(f"El pes total del paquet és de {pes_total} g")