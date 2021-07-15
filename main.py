#! /usr/bin/env python3
# -*- coding: utf-8 -*-

## Built in modules

# import numpy as np
# import numpy.random as rd
# import matplotlib.pyplot as plt
import time
# import matplotlib.cm as cm

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


## Main

def main():
    
    ## Init
    start_time = time.time()
    
    ## Run
    
    # Map creation
    m = map_modules.Map(params.MAP_LENGTH, params.MAP_WIDTH)
    m.add_life(params.LIFES)
      
    print(m.grid)

    for i in range(params.STEPS_NUMBER):
        m.tick()
        print(m.grid)
    

    end_time = time.time()
    if __name__ == "__main__" :
        print("Execution time : ",end_time-start_time)

    
"""
        
        ## Save sim as images
        
        if params.SAVE_SIM:
            fig, ax = plt.subplots()
            # ax.imshow(map + cell_map, interpolation='bilinear', cmap=cm.Greys_r)
            ax.imshow(map + cell_map, interpolation='nearest', cmap=cm.Greys_r)
            fig.savefig(sim_folder_path + "\\{:04d}".format(i))
            fig.clear()
        
        
"""
 
   
    ## End
    


## Run

if __name__ == "__main__":
    main()
