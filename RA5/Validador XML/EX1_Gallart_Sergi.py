import tkinter as tk
from tkinter import filedialog, messagebox
import json
from lxml import etree

finestra = tk.Tk()
finestra.title("XML a JSON")

fitxer_xml = None
fitxer_xsd = None
dades_json = None

def obrir_xml():
    global fitxer_xml
    fitxer_xml = filedialog.askopenfilename(filetypes=[("Fitxers XML", "*.xml")])
    if fitxer_xml:
        with open(fitxer_xml, "r", encoding="utf-8") as fitxer:
            xml_text.delete("1.0", tk.END)
            xml_text.insert(tk.END, fitxer.read())

def obrir_xsd():
    global fitxer_xsd
    fitxer_xsd = filedialog.askopenfilename(filetypes=[("Fitxers XSD", "*.xsd")])

def validar_xml():
    if not fitxer_xml or not fitxer_xsd:
        messagebox.showerror("Error", "Selecciona XML i XSD!")
        return
    try:
        print(f"Validant XML: {fitxer_xml} amb XSD: {fitxer_xsd}")
        parser = etree.XMLParser(remove_blank_text=True)
        xml_doc = etree.parse(fitxer_xml, parser)
        xsd_doc = etree.parse(fitxer_xsd, parser)
        esquema = etree.XMLSchema(xsd_doc)
        if esquema.validate(xml_doc):
            messagebox.showinfo("Validació", "XML vàlid!")
        else:
            errors = esquema.error_log
            missatge_errors = "Errors en la validació:\n" + "\n".join([str(error) for error in errors])
            print(missatge_errors)
            messagebox.showerror("Error", missatge_errors)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        print(f"Error: {e}")

def transformar_a_json():
    global dades_json
    if not fitxer_xml:
        return
    try:
        arbre = etree.parse(fitxer_xml)
        finestra_elem = arbre.getroot()
        dades = [{
            "id": llibre.get("id"),
            "titol": llibre.find("titol").text,
            "autor": llibre.find("autor").text,
            "preu": {"moneda": llibre.find("preu").get("moneda"), "quantitat": llibre.find("preu").text}
        } for llibre in finestra_elem.findall("llibre")]
        dades_json = json.dumps(dades, indent=4, ensure_ascii=False)
        json_text.delete("1.0", tk.END)
        json_text.insert(tk.END, dades_json)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
        print(f"Error en la transformació: {e}")

def desar_json():
    if not dades_json:
        return
    ruta_fitxer = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
    if ruta_fitxer:
        with open(ruta_fitxer, "w", encoding="utf-8") as fitxer:
            fitxer.write(dades_json)
        messagebox.showinfo("Desat", "JSON desat correctament!")

menubar = tk.Menu(finestra)
menu_fitxer = tk.Menu(menubar, tearoff=0)
menu_fitxer.add_command(label="Obre XML", command=obrir_xml)
menu_fitxer.add_command(label="Obre XSD", command=obrir_xsd)
menu_fitxer.add_command(label="Transforma a JSON", command=transformar_a_json)
menu_fitxer.add_separator()
menu_fitxer.add_command(label="Surt", command=finestra.quit)
menubar.add_cascade(label="Fitxer", menu=menu_fitxer)

finestra.config(menu=menubar)

tk.Button(finestra, text="Valida XML", command=validar_xml).pack(pady=5)
tk.Button(finestra, text="Desa JSON", command=desar_json).pack(pady=5)

xml_text = tk.Text(finestra, height=10, width=50)
xml_text.pack()
json_text = tk.Text(finestra, height=10, width=50)
json_text.pack()

finestra.mainloop()