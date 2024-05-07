import pygame
from cell import Cell
#This file contains the maze class, which contains the functions for generation of maze by Depth Search Algorithm
#And also storing the maze solution path in a file named path.txt
class Maze:
	def __init__(self, cols, rows):
		self.cols = cols
		self.rows = rows
		self.thickness = 4
		self.grid_cells = [Cell(col, row, self.thickness) for row in range(self.rows) for col in range(self.cols)]

	# carve grid cell walls
	def remove_walls(self, current, next):
		dx = current.x - next.x
		if dx == 1:
			current.walls['left'] = False
			next.walls['right'] = False
		elif dx == -1:
			current.walls['right'] = False
			next.walls['left'] = False
		dy = current.y - next.y
		if dy == 1:
			current.walls['up'] = False
			next.walls['down'] = False
		elif dy == -1:
			current.walls['down'] = False
			next.walls['up'] = False

	# generates maze
 # in this algo, all parts of the maze are connected.
	def generate_maze(self):
		
		current_cell = self.grid_cells[0]
		current_cells_list=[self.grid_cells[0]]
		array = []
		break_count = 1
		visited_cells=[self.grid_cells[0]]
		
		while break_count != len(self.grid_cells):
			current_cell.visited = True
			
			next_cell = current_cell.check_neighbors(self.cols, self.rows, self.grid_cells)
			
			if next_cell:
				
				
				next_cell.visited = True
				visited_cells.append(next_cell)
				break_count += 1
				array.append(current_cell)
				self.remove_walls(current_cell, next_cell)
				current_cell = next_cell
			elif array:
				current_cell = array.pop()
				

			current_cells_list.append(current_cell)

		

		for i in range(len(current_cells_list)):
			if current_cells_list[i].x==self.cols-1 and current_cells_list[i].y==self.rows-1:
				current_cells_list=current_cells_list[0:i+1]
				break
		#current_cells_list_copy=current_cells_list

		
		##this is for storing the correct maze path in path.txt

		i=0
		while (current_cells_list[i].x!=self.cols-1 or current_cells_list[i].y!=self.rows-1):
			j=i+1
			while (current_cells_list[j].x!=self.cols-1 or current_cells_list[j].y!=self.rows-1):
				if current_cells_list[i]==current_cells_list[j]:
					del current_cells_list[i:j]
					break
				j+=1
			i+=1
		
		
		
		

		
	##writing the data in the file.txt


		
		file=open('path.txt','w')
		for i in range(len(current_cells_list)-1):
			if current_cells_list[i].x>current_cells_list[i+1].x:
				file.write('l')
			elif current_cells_list[i].x<current_cells_list[i+1].x:
				file.write('r')
			elif current_cells_list[i].y>current_cells_list[i+1].y:
				file.write('u')
			elif current_cells_list[i].y<current_cells_list[i+1].y:
				file.write('d')

		file.close()

		
		
		return self.grid_cells
	
	
