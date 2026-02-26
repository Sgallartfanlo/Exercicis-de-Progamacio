import tkinter as tk

# Variable global per emmagatzemar el contingut de la pantalla de la calculadora
comptador = ""
def botons_calculadora(finestra):
    global comptador
    # Crear la pantalla de la calculadora
    pantalla = tk.Label(finestra, text=comptador, bg='white', fg='black', font=('Arial', 9, 'bold'), width=44, height=3)
    pantalla.grid(row=0, column=0, columnspan=4)

    # Funció per afegir un valor a la pantalla
    def afegir_a_pantalla(valor):
        global comptador
        comptador += str(valor)
        pantalla.config(text=comptador)

    # Funció per calcular el resultat de l'expressió a la pantalla
    def calcular():
        global comptador
        try:
            # Evalua l'expressió i actualitza la pantalla amb el resultat
            resultat = str(eval(comptador))
            comptador = resultat
            pantalla.config(text=resultat)
        except:
            # En cas d'error, esborra la pantalla i mostra "Error"
            comptador = ""
            pantalla.config(text="Error")

    # Funció per esborrar la pantalla
    def esborrar():
        global comptador
        comptador = ""
        pantalla.config(text=comptador)

    # Funcions per afegir operadors a la pantalla
    def afegir_divisio():
        afegir_a_pantalla('/')

    def afegir_multiplicacio():
        afegir_a_pantalla('*')

    def afegir_resta():
        afegir_a_pantalla('-')

    def afegir_suma():
        afegir_a_pantalla('+')

    def afegir_punt():
        afegir_a_pantalla('.')

    # Crear botons pels operadors i les altres funcions (=,C)
    divisio = tk.Button(finestra, text="/", width=10, height=5, command=afegir_divisio)
    divisio.grid(row=1, column=3)
    multiplicacio = tk.Button(finestra, text="*", width=10, height=5, command=afegir_multiplicacio)
    multiplicacio.grid(row=2, column=3)
    resta = tk.Button(finestra, text="-", width=10, height=5, command=afegir_resta)
    resta.grid(row=3, column=3)
    suma = tk.Button(finestra, text="+", width=10, height=5, command=afegir_suma)
    suma.grid(row=4, column=2)
    igual = tk.Button(finestra, text="=", width=10, height=5, command=calcular)
    igual.grid(row=4, column=3)
    punt = tk.Button(finestra, text=".", width=10, height=5, command=afegir_punt)
    punt.grid(row=4, column=1)
    c = tk.Button(finestra, text="C", width=44, height=3, command=esborrar)
    c.grid(row=5, column=0, columnspan=4)

def numeros(finestra):
    # Funció per afegir un valor a la pantalla
    def afegir_a_pantalla(valor):
        global comptador
        comptador += str(valor)
        finestra.children['!label'].config(text=comptador)

    # Funcions per afegir els números a la pantalla
    def afegir_zero():
        afegir_a_pantalla('0')

    def afegir_un():
        afegir_a_pantalla('1')

    def afegir_dos():
        afegir_a_pantalla('2')

    def afegir_tres():
        afegir_a_pantalla('3')

    def afegir_quatre():
        afegir_a_pantalla('4')

    def afegir_cinc():
        afegir_a_pantalla('5')

    def afegir_sis():
        afegir_a_pantalla('6')

    def afegir_set():
        afegir_a_pantalla('7')

    def afegir_vuit():
        afegir_a_pantalla('8')

    def afegir_nou():
        afegir_a_pantalla('9')

    # Crear botons per a cada número
    zero = tk.Button(finestra, text="0", width=10, height=5, command=afegir_zero)
    zero.grid(row=4, column=0)
    un = tk.Button(finestra, text="1", width=10, height=5, command=afegir_un)
    un.grid(row=3, column=0)
    dos = tk.Button(finestra, text="2", width=10, height=5, command=afegir_dos)
    dos.grid(row=3, column=1)
    tres = tk.Button(finestra, text="3", width=10, height=5, command=afegir_tres)
    tres.grid(row=3, column=2)
    quatre = tk.Button(finestra, text="4", width=10, height=5, command=afegir_quatre)
    quatre.grid(row=2, column=0)
    cinc = tk.Button(finestra, text="5", width=10, height=5, command=afegir_cinc)
    cinc.grid(row=2, column=1)
    sis = tk.Button(finestra, text="6", width=10, height=5, command=afegir_sis)
    sis.grid(row=2, column=2)
    set = tk.Button(finestra, text="7", width=10, height=5, command=afegir_set)
    set.grid(row=1, column=0)
    vuit = tk.Button(finestra, text="8", width=10, height=5, command=afegir_vuit)
    vuit.grid(row=1, column=1)
    nou = tk.Button(finestra, text="9", width=10, height=5, command=afegir_nou)
    nou.grid(row=1, column=2)

# S'ha utilitzat una variable global per emmagatzemar el contingut de la pantalla de la calculadora, 
# permetent un accés compartit i simplificant el codi.