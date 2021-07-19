#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## Built in modules

# import numpy as np
# import numpy.random as rd
# import matplotlib.pyplot as plt
import time
# import matplotlib.cm as cm
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
        
        # Grille
        self.disp = display_modules.Display(root, self.m)
        
        # Bouton play
        tk.Button(root, text="play", command=self.play).pack()
        
        # Display pattern initial
        self.display()
        
    def play(self):
        self.m.tick()
        print(self.m.grid)
        self.display()
    
    def display(self):
        g = self.m.grid
        for r in range(params.MAP_HEIGHT):
            for c in range(params.MAP_WIDTH):
                # si g[r, c] == 0 alors faire kill life
                if g[r, c] == 0:
                    self.disp.kill(r, c)
                # si == 100 alors bring life
                if g[r, c] == params.LIFE_VALUE:
                    self.disp.bring_life(r, c)
        
    

def main():
    root = tk.Tk()
    #root.minsize(840, 400)
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()


## Main
"""
class Main():
    
    def __init__(self):
        self.m = map_modules.Map()
        self.disp = display_modules.Display(self)
        
    def tick(self):
        self.m.tick()
        self.disp.show()
        
        """
    

"""
def main():
    
    ## Init
    start_time = time.time()
    
    ## Run
    
    # Map creation (back)
    m = map_modules.Map()
    
    # Launch display (front)
    display_modules.Display(m)



    

    
    for i in range(params.STEPS_NUMBER):
        m.tick()
        print(m.grid)
    

    end_time = time.time()
    if __name__ == "__main__" :
        print("Execution time : ",end_time-start_time)

    

        
        ## Save sim as images
        
        if params.SAVE_SIM:
            fig, ax = plt.subplots()
            # ax.imshow(map + cell_map, interpolation='bilinear', cmap=cm.Greys_r)
            ax.imshow(map + cell_map, interpolation='nearest', cmap=cm.Greys_r)
            fig.savefig(sim_folder_path + "\\{:04d}".format(i))
            fig.clear()
        
       
 
   
    ## End
    
"""

## Run
"""
if __name__ == "__main__":
    display_modules.Display(map_modules.Map())
"""