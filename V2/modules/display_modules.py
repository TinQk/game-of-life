#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import params
import main
import numpy as np

# Display map with tkinter
class Display:
    
    def __init__(self, root, m):

        self.root = root

        # Canvas principal
        self.c = tk.Canvas(self.root, width=params.SCREEN_WIDTH, height=params.SCREEN_HEIGHT, borderwidth=5, background='blue')
        
        # Create the mouse click event binding
        self.c.bind("<Button-1>", callback)
        self.c.pack()
        
        self.c.m = m
        
        # Create a grid of white rectangles and store the references
        self.c.tiles = self.create_tiles()
        
    
    def create_tiles(self):
        row = params.MAP_HEIGHT
        col = params.MAP_WIDTH
        col_width = params.SCREEN_WIDTH/col
        row_height = params.SCREEN_HEIGHT/row
        
        tiles = np.zeros((row, col))
        for r in range(row):
            for c in range(col):
                tiles[r][c] = self.c.create_rectangle(c*col_width, r*row_height, (c+1)*col_width, (r+1)*row_height, fill="red")
        
                
        return tiles
        
    
    def update(self, dif_grid):
        for r in range(params.MAP_HEIGHT):
            for c in range(params.MAP_WIDTH):
                if dif_grid[r][c] == params.LIFE_VALUE:
                    self.bring_life(r, c)
                if dif_grid[r][c] == -params.LIFE_VALUE:
                    self.kill(r, c)

        
    def kill(self, row, col):
        if not self.c.tiles[row][col]:
            return
        else:
            self.c.delete(self.c.tiles[row][col])
            self.c.tiles[row][col] = None
            
    def bring_life(self, row, col):
        col_width = params.SCREEN_WIDTH/params.MAP_WIDTH
        row_height = params.SCREEN_HEIGHT/params.MAP_HEIGHT
        if not self.c.tiles[row][col]:
            self.c.tiles[row][col] = self.c.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
            
        
    

def callback(click):
    # Get rectangle diameters
    col_width = click.widget.winfo_width()/params.MAP_WIDTH
    row_height = click.widget.winfo_height()/params.MAP_HEIGHT
    
    # Calculate column and row number
    col = int(click.x//col_width)
    row = int(click.y//row_height)
    
    # If the tile is not filled, create a rectangle and store its id in "tiles"
    if not click.widget.tiles[row][col]:
        click.widget.tiles[row][col] = click.widget.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
        # changer la map
        click.widget.m.grid[row][col] = params.LIFE_VALUE
        
    # If the tile is filled, delete the rectangle and clear the reference
    else:
        click.widget.delete(click.widget.tiles[row][col])
        click.widget.tiles[row][col] = None
        # changer la map
        click.widget.m.grid[row][col] = 0

        
        
