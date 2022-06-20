
'''
	My Solution to the Programing Project of Chapter 4:
		Using a sparse matrix to impliment Game of Life grid.
		The sparse matrix  contains only living cells.

'''


class _Cell:
	def __init__(self, row, col, value):
		self.row = row
		self.col = col
		self.life = value 

	def pos(self):
		return tuple((self.row, self.col))

	def __repr__(self):

		return str((self.row, self.col))

# Infinite Grid Matrix using a list
class SparseLifeGrid:
	# Defines constants to represent the cell states.
	DEAD_CELL = 0
	LIVE_CELL = 1

	def __init__(self, nrows, ncols):
		self._nrows = nrows	
		self._ncols = ncols	
		self._elementList = list()


	def nRows(self):
		return self._nrows	

	def nCols(self):
		return self._ncols	

	def minRange(self):
		minim = self._elementList[0]
		for cell in self._elementList:
			if (minim.row > cell.row) and (minim.col > cell.row) and (minim.life == self.LIVE_CELL):
				minim = cell
		return (minim.row, minim.col)

	def maxRange(self):
		minim = self._elementList[0]
		for cell in self._elementList:
			if (minim.row <= cell.row) or (minim.col <= cell.row) and (minim.life == self.LIVE_CELL):
				minim = cell
		return (minim.row, minim.col)


	# This function is O(n) complexity
	def configure(self, coordList):
		# Empty the elements before configure

		for i in range(len(self)):
			self._elementList.pop()

		# Sets the coordinate to life in the grid.
		for coord in coordList:
			self.setCell(coord[0], coord[1])


	def setCell(self, row, col):
		self[row, col] = self.LIVE_CELL


	def clearCell(self, row, col):
		self[row, col] = self.DEAD_CELL


	def isLiveCell(self, row, col):
		LiveCell = self[row, col]
		if LiveCell is not None:
			return LiveCell.life == SparseLifeGrid.LIVE_CELL
		return False

	def numLiveNeighbors(self, row, col):

		'''
		A cell has 8 neighbors, so we need to check for 8 positions
		around the cell to see how many is alive.
			[0	0	1]
			[0	[1]	0]
			[0	1	0]
		so [1] has 2 neighbors.

	 	'''

		numb = 0
		# Left
		if self.isLiveCell(row-1, col):
			numb +=1

		# Right
		if self.isLiveCell(row+1, col):
			numb +=1

		# Top
		if self.isLiveCell(row, col-1):
			numb +=1 

		# Bottom
		if self.isLiveCell(row, col +1):
			numb +=1

		# Bottom Right
		if self.isLiveCell(row+1, col+1):
			numb +=1

		# Bottom Left
		if self.isLiveCell(row -1, col +1):
			numb +=1

		# Top Left
		if self.isLiveCell(row -1, col-1):
			numb+=1

		# Top Right
		if self.isLiveCell(row +1, col -1):
			numb +=1

		return numb


	def __len__(self):
		return len(self._elementList)

	def __getitem__(self, ndxTuple):
		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:
			return self._elementList[ndx]
		return None

	def __setitem__(self, ndxTuple, scalar):
		'''
		we can only accept live cells, so we check if the index (ndx) is
		in the _elementList, if we kill the cell by popping it off
		the _elementList.

		if ndx is not in the _elementList and we want to give it life 
		we add a new cell to the _elementList of live cells
		'''

		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:
			if scalar == self.DEAD_CELL:
				self._elementList.pop(ndx)

		else:
			if scalar == self.LIVE_CELL:
				element = _Cell(ndxTuple[0], ndxTuple[1], scalar)
				self._elementList.append(element)



	def _findPosition(self, row, col):
		n = len(self._elementList)
		for i in range(n):
			if row == self._elementList[i].row and col == self._elementList[i].col:
				return i 
		return None

if __name__ == '__main__':

	INIT_CONFIG = [(1,1), (1,2),(2,2), (3,2)]
	INIT_CONFIG = [(0,1),(1,2),(2,2),(3,2),(3,1),(3,0)]

	

	grid = SparseLifeGrid(50,50)
	grid[1,1] = 1
	print(grid._elementList)
	print(grid.numLiveNeighbors(2,2))