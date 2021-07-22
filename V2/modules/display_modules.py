#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import params as p

# Display map with tkinter
class Interface:
    
    def __init__(self, root, m):

        self.root = root

        # Canvas principal (acceuille la grille)
        self.c = tk.Canvas(self.root, width=p.SCREEN_WIDTH, height=p.SCREEN_HEIGHT, borderwidth=0, background='white')
        
        # link back map to canvas
        self.c.m = m
        
        # Create a grid of white rectangles and store the references
        self.c.tiles = self.create_tiles()
        
        # Create the mouse click event binding
        self.c.bind("<Button-1>", 
                    lambda event, test="test": 
                        self.click_grid(event, test))
        self.c.pack()

        # Bouton play
        tk.Button(self.root, text="play", command=self.play).pack()
        
        # Bouton print
        tk.Button(self.root, text="print", command=self.print).pack()
        
        
    def click_grid(self, event, test):
        # Calculate column and row number
        col = int(event.x//p.COL_SIZE)
        row = int(event.y//p.ROW_SIZE)
        
        # If the cell is alive, kill it
        if self.c.tiles[row][col].alive:
            self.c.tiles[row][col].kill()
            
        # If the cell is dead, give it life
        else:
            self.c.tiles[row][col].give_life()
            
            
    def play(self):
        dif_grid = self.c.m.tick()
        self.update(dif_grid)
        
    def print(self):
        print(self.c.m.grid)
        
    
    def create_tiles(self):
        row = p.ROWS
        col = p.COLUMNS
        
        tiles = []
        for r in range(row):
            a = []
            for c in range(col):
                a.append(Cell(self.c, (r, c)))
            tiles.append(a)
        return tiles
        
    
    def update(self, dif_grid):
        for r in range(p.ROWS):
            for c in range(p.COLUMNS):
                if dif_grid[r][c] == p.LIFE_VALUE:
                    self.c.tiles[r][c].give_life()
                if dif_grid[r][c] == -p.LIFE_VALUE:
                    self.c.tiles[r][c].kill()
                    
    
        
class Cell:
    
    def __init__(self, canvas, coords):
        self.c = canvas
        self.coords = coords
        r, c = self.coords
        self.ref = canvas.create_rectangle(c*p.COL_SIZE, r*p.ROW_SIZE, (c+1)*p.COL_SIZE, (r+1)*p.ROW_SIZE, fill="white")
        self.alive = False
    
    def give_life(self):
        r, c = self.coords
                
        # création d'un rectangle noir
        self.ref = self.c.create_rectangle(c*p.COL_SIZE, r*p.ROW_SIZE, (c+1)*p.COL_SIZE, (r+1)*p.ROW_SIZE, fill="black")
        
        self.alive = True

        # changer la map
        self.c.m.grid[r][c] = p.LIFE_VALUE
      
    
    def kill(self):
        r, c = self.coords
        
        self.c.delete(self.ref) # destruction du rectangle noir
        
        self.ref = None
        self.alive = False
        
        # changer la map
        self.c.m.grid[r][c] = 0
      
        
        
