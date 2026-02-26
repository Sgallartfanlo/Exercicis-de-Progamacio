import tkinter as tk

# Crear la finestra principal
finestra = tk.Tk()
finestra.title("Clicker de Galetes")
finestra.geometry("500x400")

# Variables del joc
galetes = 0
gps = 0  # Galetes per segon

# Costos i quantitats d'eines
cost_eines = [10, 50, 200]
eines_posseides = [0, 0, 0]
produccio_rates = [1, 5, 20]

def clicar_galeta():
    global galetes
    galetes += 1
    actualitzar_labels()

def comprar_eina(index):
    global galetes, gps
    if galetes >= cost_eines[index]:
        galetes -= cost_eines[index]
        eines_posseides[index] += 1
        gps += produccio_rates[index]
        cost_eines[index] = int(cost_eines[index] * 1.5)  # Augmenta el cost
        actualitzar_labels()
        actualitzar_botons()

def produccio_automatica():
    global galetes
    galetes += gps
    actualitzar_labels()
    finestra.after(1000, produccio_automatica)

def actualitzar_labels():
    galetes_label.config(text=f"Galetes: {galetes}")
    gps_label.config(text=f"Galetes per segon: {gps}")

def actualitzar_botons():
    for i in range(3):
        eina_botons[i].config(text=f"Eina {i+1} ({cost_eines[i]} galetes) - {eines_posseides[i]}x")

# Widgets
galetes_label = tk.Label(finestra, text="Galetes: 0", font=("Arial", 16))
galetes_label.pack(pady=10)

gps_label = tk.Label(finestra, text="Galetes per segon: 0", font=("Arial", 14))
gps_label.pack(pady=5)

# Botó de clic
clic_boto = tk.Button(finestra, text="🍪 Clica!", font=("Arial", 14), command=clicar_galeta)
clic_boto.pack(pady=10)

# Botons d'eines
eina_botons = []
for i in range(3):
    btn = tk.Button(finestra, text=f"Eina {i+1} ({cost_eines[i]} galetes)", command=lambda i=i: comprar_eina(i))
    btn.pack(pady=5)
    eina_botons.append(btn)

# Iniciar producció automàtica
finestra.after(1000, produccio_automatica)

# Executar l'aplicació
finestra.mainloop()