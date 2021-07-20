#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## Built in modules

import tkinter as tk
import os
import sys

## Project modules

main_dir_path = os.getcwd()
modules_path = main_dir_path + "\\modules"

# On ajoute le dossier modules aux dossiers de recherche des modules
if modules_path not in sys.path:
    sys.path.append(modules_path)

import map_modules
import params
import display_modules

class App():
    def __init__(self, root):
        # init map en back
        self.m = map_modules.Map()
        self.m.load_lifes(params.LIFES)
        
        # init affichage grille
        self.disp = display_modules.Display(root, self.m)
        
        # Bouton play
        tk.Button(root, text="play", command=self.play).pack()
        
        # Display pattern initial
        self.disp.update(-1*self.m.grid)
        
    def play(self):
        dif_grid = self.m.tick()
        print(self.m.grid)
        self.disp.update(dif_grid)
    

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()

