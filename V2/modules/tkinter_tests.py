# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:22:40 2021

@author: Quentin
"""

def tick():
    return print("hello world")

import tkinter as tk
import tkinter.ttk as ttk

ROWS = 30
COLUMNS = 30

# Première fenêtre
window = tk.Tk()

# Personnalisation
window.title("Game of Life")
window.geometry("600x600")
#window.minsize(900, 900)
#window.config(background='white')

# Créer une frame
frame = tk.Frame(window, bg="blue", bd=1, relief="sunken")
# Ajouter un texte
label_title = tk.Label(frame, text="Credit : Conway", font=("Arial", 40))
label_title.pack(expand=True)
frame.pack()

# Ajouter un premier bouton
play_button = tk.Button(window, text="play", command=tick)
play_button.pack()



# Créer et configurer la frame qui va contenir la grille
grid_frame = tk.Frame(window)
grid_frame.pack(fill="both")

cell_style = ttk.Style()

cell_style.configure('empty_cell', foreground = 'red')

# Ajouter une grille
for r in range(ROWS):
    #tk.Grid.rowconfigure(grid_frame, r, weight=1)
    for c in range(COLUMNS):
        #tk.Grid.columnconfigure(grid_frame, c, weight=1)
        tk.Canvas(grid_frame, bg="red").grid(row=r, column=c, sticky="NSEW")
        #tk.Button(grid_frame).grid(row=r, column=c, sticky="NSEW")


# Affichage
window.mainloop()



"""
label = tk.Label(fenetre, text="Hello World")
label.pack()

bouton = tk.Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()

menubar = tk.Menu(fenetre)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

"""