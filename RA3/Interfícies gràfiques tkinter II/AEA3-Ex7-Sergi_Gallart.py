import tkinter as tk

# Crear la finestra principal
finestra = tk.Tk()
finestra.title("Clicker de Dorayakis")
finestra.geometry("500x650")
photo = tk.PhotoImage(file="Foto.png")
finestra.configure(bg="#6089e1")

# Variables del joc
Dorayakis = 0
gps = 0  # Dorayakis per segon

# Costos i quantitats d'eines
cost_eines = [10, 50, 200]
eines_posseides = [0, 0, 0]
produccio_rates = [1, 5, 20]

def clicar_dorayaki():
    global Dorayakis
    Dorayakis += 1
    actualitzar_labels()

def comprar_eina(index):
    global Dorayakis, gps
    if Dorayakis >= cost_eines[index]:
        Dorayakis -= cost_eines[index]
        eines_posseides[index] += 1
        gps += produccio_rates[index]
        cost_eines[index] = int(cost_eines[index] * 1.5)  # Augmenta el cost
        actualitzar_labels()
        actualitzar_botons()

def produccio_automatica():
    global Dorayakis
    Dorayakis += gps
    actualitzar_labels()
    finestra.after(1000, produccio_automatica)

def actualitzar_labels():
    Dorayakis_label.config(text=f"Dorayakis: {Dorayakis}",bg="#6089e1",font=("Arial", 14,"bold"))
    gps_label.config(text=f"Dorayakis per segon: {gps}",bg="#6089e1",font=("Arial", 14,"bold"))

def actualitzar_botons():
    for i in range(3):
        if i == 0:
            eina_botons[i].config(text=f"Porta Màgica ({cost_eines[i]} Dorayakis) - {eines_posseides[i]}x", command=comprar_eina_0,font=("Arial", 11))
        elif i == 1:
            eina_botons[i].config(text=f"Casquet Volador({cost_eines[i]} Dorayakis) - {eines_posseides[i]}x", command=comprar_eina_1,font=("Arial", 11))
        elif i == 2:
            eina_botons[i].config(text=f"Llanterna Minimitzadora({cost_eines[i]} Dorayakis) - {eines_posseides[i]}x", command=comprar_eina_2,font=("Arial", 11))

def comprar_eina_0():
    comprar_eina(0)

def comprar_eina_1():
    comprar_eina(1)

def comprar_eina_2():
    comprar_eina(2)

# Widgets
Dorayakis_label = tk.Label(finestra, text="Dorayakis: 0", font=("Arial", 16,"bold"), bg="#6089e1")
Dorayakis_label.pack(pady=10)

gps_label = tk.Label(finestra, text="Dorayakis per segon: 0", font=("Arial", 14,"bold"), bg="#6089e1")
gps_label.pack(pady=5)

# Botó de clic
clic_boto = tk.Button(finestra, image=photo, font=("Arial", 14), command=clicar_dorayaki)
clic_boto.pack(pady=10)

# Etiqueta de "Eines"
eines_label = tk.Label(finestra, text="Invents:", font=("Arial", 14,"bold"), bg="#6089e1")
eines_label.pack(pady=10)

# Botons d'eines
eina_botons = []
for i in range(3):
    btn = tk.Button(finestra, text=f"Dorayakis {i+1} ({cost_eines[i]} Dorayakis)")
    btn.pack(pady=5)
    eina_botons.append(btn)

actualitzar_botons()

# Iniciar producció automàtica
finestra.after(1000, produccio_automatica)

# Executar l'aplicació
finestra.mainloop()