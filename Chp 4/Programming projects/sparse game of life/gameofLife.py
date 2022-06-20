from sparseLifeGame import SparseLifeGrid


# Slider Gun
INIT_CONFIG = [(1,5),(2,5),(1,6),(2,6),(35,3),(36,3),(35,4),(36,4),\

				(11,5),(11,6),(11,7),(12,4),(13,3),(14,3),(16,4),
				(17,5),(17,6),(17,7),(15,6),(18,6),(16,8),(14,9),
				(13,9),(12,8),\

				(21,3),(21,4),(21,5),(22,3),(22,4),(22,5),(23,2),
				(23,6),(25,1),(25,2),(25,6),(25,7)
]
INIT_CONFIG = [(1,2), (2,1),(2,2), (2,3),(5,5)]


# Indicate the number of generations.
NUM_GENS = 8


def main():
	n =5
	grid = SparseLifeGrid(n,n)
	grid.configure(INIT_CONFIG)
	for i in range(NUM_GENS):
		grid.configure(evolve(grid))
		draw(grid)


def debug(grid):
	# Used to display the number of live cells in a generation

	print(str(len(grid)), end = '')
	print('\b' * len(str(grid)),flush = True, end = '')

def checkCondition(grid, pos):
	'''
		Helper function to impliment the rules
	'''
	if pos < (grid.nRows(), grid.nCols()) and (pos[0]>=0 and pos[1] >= 0):
		neighbors = grid.numLiveNeighbors(pos[0], pos[1])
		if(neighbors == 2 and grid.isLiveCell(pos[0], pos[1])) or (neighbors == 3):
			return True
	return False


def evolve(grid):

	'''
		Loop through the entire grid of live cells, 
		for each live cell impliment the rules for the 
		8 neighbors around it and itself.

	'''
	liveCells = list()
	for i in range(len(grid)):
		cell = grid._elementList[i].pos()
		if checkCondition(grid,cell):
			liveCells.append(cell)

		# To do: Prevent reoccuring cells from being append to the liveCells

		# Left
		if checkCondition(grid, (cell[0]-1, cell[1])):
			liveCells.append((cell[0]-1, cell[1]))

		# Right
		if checkCondition(grid, (cell[0]+1, cell[1])):
			liveCells.append((cell[0]+1, cell[1]))

		# Top
		if checkCondition(grid, (cell[0], cell[1]-1)):
			liveCells.append((cell[0], cell[1]-1))

		# Bottom
		if checkCondition(grid, (cell[0], cell[1] + 1)):
			liveCells.append((cell[0], cell[1]+1))

		# Bottom Right
		if checkCondition(grid, (cell[0]+1, cell[1] + 1)):
			liveCells.append((cell[0]+1, cell[1] + 1))

		# Bottom Left
		if checkCondition(grid, (cell[0] -1, cell[1] + 1)):
			liveCells.append((cell[0] -1, cell[1] + 1))

		# Top Left
		if checkCondition(grid, (cell[0] -1, cell[1] -1)):
			liveCells.append((cell[0] -1, cell[1] -1))

		# Top Right
		if checkCondition(grid, (cell[0] +1, cell[1] -1)):
			liveCells.append((cell[0] +1, cell[1] -1))


	# To lazy to prevent reoccuring cells, pls help
	liveCells = set(liveCells)
	return list(liveCells)




def draw(grid):
	for i in range(grid.nRows()):
		for j in range(grid.nCols()):
			cell = grid[i,j]
			if cell is not None:
				if grid.isLiveCell(cell.row, cell.col):
					print(1, end = '\t')

				else:
					print(0, end ='\t')
			else:
				print(0, end= "\t")
		print("")
	print('\n')

if __name__ == "__main__":
	main()