import pygame
from random import choice

class Cell:
	#This file contains the basic class Cell. This class contains the properties of each cell of the grid of the maze. 
 	#The basic declaration of the Cell contains its x and y indices, and the thickness of wall around it. 
  	#This also contains some functions for the generation of the maze which is done in maze.py file.
	def __init__(self, x, y, thickness):
		#here x and y are not actual coordinates but just indices of the row or column respectively.
		self.x, self.y = x, y
		self.thickness = thickness
		self.walls = {'up': True, 'right': True, 'down': True, 'left': True}
		self.visited = False

	# draw grid cell walls
	def draw(self, sc, tile):
		x, y = self.x * tile, self.y * tile
		if self.walls['up']:
			pygame.draw.line(sc, pygame.Color("#322001"), (x, y), (x + tile, y), self.thickness)
		if self.walls['right']:
			pygame.draw.line(sc, pygame.Color("#322001"), (x + tile, y), (x + tile, y + tile), self.thickness)
		if self.walls['down']:
			pygame.draw.line(sc, pygame.Color("#322001"), (x + tile, y + tile), (x , y + tile), self.thickness)
		if self.walls['left']:
			pygame.draw.line(sc, pygame.Color("#322001"), (x, y + tile), (x, y), self.thickness)

	# checks if cell does exist and returns it if it does
	def check_cell(self, x, y, cols, rows, grid_cells):
		find_index = lambda x, y: x + y * cols
		if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:
			return False
		return grid_cells[find_index(x, y)]

	# checking cell neighbors of current cell if visited (carved) or not
	def check_neighbors(self, cols, rows, grid_cells):
		neighbors = []
		up = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
		right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
		down = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
		left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
		if up and not up.visited:
			neighbors.append(up)
		if right and not right.visited:
			neighbors.append(right)
		if down and not down.visited:
			neighbors.append(down)
		if left and not left.visited:
			neighbors.append(left)
		return choice(neighbors) if neighbors else False
	
	
	
	