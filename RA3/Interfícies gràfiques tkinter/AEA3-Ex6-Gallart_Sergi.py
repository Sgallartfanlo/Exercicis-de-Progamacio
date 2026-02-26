import tkinter as tk
import llibreria_calc as lib #Importem la llibreria personalitzada i li assignem un alies

finestra = tk.Tk() #Definim la finestra
finestra.title("Calculadora")

lib.botons_calculadora(finestra)   #Invoquem les funcions
lib.numeros(finestra)
finestra.mainloop()
#Ho he realitzat amb una llibreria a part degut a que queda mès ordenat