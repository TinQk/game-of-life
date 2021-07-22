#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import params

class Map:
    
    def __init__(self):
        self.height = params.ROWS
        self.width = params.COLUMNS
        self.grid = np.zeros((self.height, self.width))
        
    def load_lifes(self, life_locations):
        for loc in life_locations:
            self.grid[loc[0], loc[1]] = params.LIFE_VALUE
            
    def tick(self):
        ### UPDATE MATRICE after 1 tick
        old_grid = self.grid
        
        g = self.grid + game_of_life_weight_grid(self.grid) / 100
        sh = g.shape

        self.grid = ((g == np.full(sh, 3)) + (g == np.full(sh, 102)) + (g == np.full(sh, 103))) * np.ones(sh) * 100
        
        return self.grid - old_grid
        

## Other functions
def botline_to_top(m):
    [top, bot] = np.split(m, [m.shape[0]-1], axis=0)
    return np.vstack((bot, top))

def topline_to_bot(m):
    [top, bot] = np.split(m, [1], axis=0)
    return np.vstack((bot, top))

def rightcol_to_left(m):
    [left, right] = np.split(m, [m.shape[1]-1], axis=1)
    return np.hstack((right, left))

def leftcol_to_right(m):
    [left, right] = np.split(m, [1], axis=1)
    return np.hstack((right, left))

def game_of_life_weight_grid(g):
    # Somme des 8 matrices décalées :
    return (topline_to_bot(g)
            + topline_to_bot(rightcol_to_left(g))
            + rightcol_to_left(g)
            + rightcol_to_left(botline_to_top(g))
            + botline_to_top(g)
            + botline_to_top(leftcol_to_right(g))
            + leftcol_to_right(g)
            + leftcol_to_right(topline_to_bot(g))
            )
