import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io
import sqlite3

# Funció per obtenir els noms dels Pokémon de la primera generació
def obtenir_llista_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')
    if response.status_code == 200:
        data = response.json()
        return [pokemon['name'] for pokemon in data['results']]
    else:
        return []

# Llistat de Pokémon de la primera generació
pokemon_list = obtenir_llista_pokemon()

# Funció per obtenir la informació dels Pokémon
def obtenir_dades_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Funció per carregar la imatge del Pokémon
def carregar_imatge_pokemon(pokemon):
    dades = obtenir_dades_pokemon(pokemon)
    if dades:
        sprite_url = dades['sprites']['front_default']
        response = requests.get(sprite_url)
        if response.status_code == 200:
            img_data = response.content
            img = Image.open(io.BytesIO(img_data))
            return ImageTk.PhotoImage(img)
    return None

# Funció per actualitzar la imatge del Pokémon seleccionat
def actualitzar_imatge_pokemon(event=None):
    pokemon1 = variable_pokemon1.get()
    imatge1 = carregar_imatge_pokemon(pokemon1)
    if imatge1:
        label_pokemon1.config(image=imatge1)
        label_pokemon1.image = imatge1

    pokemon2 = variable_pokemon2.get()
    imatge2 = carregar_imatge_pokemon(pokemon2)
    if imatge2:
        label_pokemon2.config(image=imatge2)
        label_pokemon2.image = imatge2

# Funció per mostrar les imatges dels Pokémon seleccionats
def mostrar_imatges():
    actualitzar_imatge_pokemon()

# Funció per calcular el resultat del combat
def calcular_guanyador(pokemon1, pokemon2):
    stats1 = obtenir_dades_pokemon(pokemon1)['stats']
    stats2 = obtenir_dades_pokemon(pokemon2)['stats']
    
    puntuació1 = sum(stat['base_stat'] for stat in stats1)
    puntuació2 = sum(stat['base_stat'] for stat in stats2)
    
    if puntuació1 > puntuació2:
        return pokemon1
    else:
        return pokemon2

# Funció per gestionar la base de dades
def actualitzar_base_dades(guanyador):
    conn = sqlite3.connect('combats_pokemon.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS victories 
                      (pokemon TEXT, victòries INTEGER)''')
    cursor.execute('''INSERT OR IGNORE INTO victories (pokemon, victòries) 
                      VALUES (?, 0)''', (guanyador,))
    cursor.execute('''UPDATE victories SET victòries = victòries + 1 
                      WHERE pokemon = ?''', (guanyador,))
    conn.commit()
    conn.close()

# Funció per mostrar el Saló de la Fama
def mostrar_salo_fama():
    conn = sqlite3.connect('combats_pokemon.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT pokemon, victòries FROM victories 
                      ORDER BY victòries DESC LIMIT 5''')
    registres = cursor.fetchall()
    conn.close()
    
    finestra_salo_fama = tk.Toplevel(root)
    finestra_salo_fama.title("Saló de la Fama")
    
    for i, (pokemon, victòries) in enumerate(registres):
        tk.Label(finestra_salo_fama, text=f"{i+1}. {pokemon} - {victòries} victòries").pack()

# Funció per iniciar el combat
def iniciar_combat():
    pokemon1 = variable_pokemon1.get()
    pokemon2 = variable_pokemon2.get()
    
    if pokemon1 == pokemon2:
        messagebox.showerror("Error", "No es poden seleccionar el mateix Pokémon")
        return
    
    guanyador = calcular_guanyador(pokemon1, pokemon2)
    actualitzar_base_dades(guanyador)
    
    messagebox.showinfo("Resultat del combat", f"El guanyador és: {guanyador.capitalize()}")

# Configuració de la interfície gràfica
root = tk.Tk()
root.title("Combats Pokémon")
root.geometry("600x400")  # Ajusta la mida de la finestra aquí

tk.Label(root, text="Pokémon 1:").pack()
variable_pokemon1 = tk.StringVar(root)
variable_pokemon1.set(pokemon_list[0])  # Valor per defecte
desplegable_pokemon1 = tk.OptionMenu(root, variable_pokemon1, *pokemon_list)
desplegable_pokemon1.pack()

label_pokemon1 = tk.Label(root)
label_pokemon1.pack()

tk.Label(root, text="Pokémon 2:").pack()
variable_pokemon2 = tk.StringVar(root)
variable_pokemon2.set(pokemon_list[0])  # Valor per defecte
desplegable_pokemon2 = tk.OptionMenu(root, variable_pokemon2, *pokemon_list)
desplegable_pokemon2.pack()

label_pokemon2 = tk.Label(root)
label_pokemon2.pack()

tk.Button(root, text="Mostrar imatges", command=mostrar_imatges).pack()
tk.Button(root, text="Iniciar combat", command=iniciar_combat).pack()
tk.Button(root, text="Saló de la Fama", command=mostrar_salo_fama).pack()

root.mainloop()