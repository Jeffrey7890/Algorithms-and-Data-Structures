# Implements the LifeGrid ADT for use with the game of Life.
from Array2D import Array2D

class GameGrid:
	# Defines constants to represent the cell states.
	DEAD_CELL = 0
	LIVE_CELL = 1

	# Creates the game grid and initializes the cells to dead.
	def __init__(self, numRows, numCols):
		# Allocate the 2-D array for the grid.
		self._grid = Array2D(numRows, numCols)
		# Clear the grid and set all cells to dead.
		self.configure(list())

	# Return the number of rows in the grid.
	def numRows(self):
		return self._grid.numRows()

	# Returns the number of columns in the grid.
	def numCols(self):
		return self._grid.numCols()

	# Configures the grid to contain the given live cells.
	def configure(self, coordList):
		# Clear the game grid.
		for i in range(self.numRows()):
			for j in range(self.numCols()):
				self.clearCell(i,j)

		# Set the indicated cells to be alive.
		for coord in coordList:
			self.setCell(coord[0], coord[1])

	# Does the indicated cell contain a live organism?
	def isLiveCell(self, row, col):
		return self._grid[row, col] == GameGrid.LIVE_CELL

	# Clears the indicated cell by setting it to dead.
	def clearCell(self, row, col):
		self._grid[row, col] = GameGrid.DEAD_CELL

	# Sets the indicated cell to be alive.
	def setCell(self, row, col):
		self._grid[row, col] = GameGrid.LIVE_CELL

	# Returns the number of live neighbors for the given cell.
	def numLiveNeighbors(self, row, col):
		numb = 0
		numRow = self.numRows()
		numCols = self.numCols()

		# Left
		if (row - 1) >= 0 and self.isLiveCell(row-1, col):
			numb+=1

		# Right
		if (row + 1) < numRow and self.isLiveCell(row+1, col):
			numb+=1

		# Top
		if (col - 1) >= 0 and self.isLiveCell(row, col-1):
			numb+=1

		# Bottom
		if (col + 1) < numCols and self.isLiveCell(row, col+1):
			numb +=1 

		# Bottom Right
		if (col + 1) < numCols and (row + 1) < numRow and self.isLiveCell(row+1, col+1):
			numb+=1 

		# Bottom Left
		if (col + 1) < numCols and (row -1 ) >= 0 and self.isLiveCell(row-1, col+1):
			numb += 1

		# Top Left
		if ( col -1) >= 0 and (row -1 ) >= 0 and self.isLiveCell(row-1, col-1): 
			numb +=1 

		# Top Right
		if (col - 1) >= 0 and (row + 1) < numRow and self.isLiveCell(row+1, col-1):
			numb +=1

		return numb

	def __getitem__(self, ndxTuple):
		return self._grid[ndxTuple[0], ndxTuple[1]]

if __name__ == "__main__":

	GRID_WIDTH = 5
	GRID_HEIGHT = 5

	INIT_CONFIG = [(1,1), (1,2),(2,2), (3,2)]


	grid = GameGrid(GRID_WIDTH, GRID_HEIGHT)
	grid.configure(INIT_CONFIG)

	print(grid.numLiveNeighbors(2,2))

	



