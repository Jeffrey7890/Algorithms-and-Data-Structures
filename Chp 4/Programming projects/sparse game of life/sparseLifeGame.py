# Implements the LifeGrid ADT with an Infinite grid
# using a sparse matrix technique


class _Cell:
	def __init__(self, row, col, value):
		self.row = row
		self.col = col
		self.life = value 
	def __repr__(self):

		return str((self.row, self.col))

# Infinite Grid Matrix using a list
class SparseLifeGrid:
	# Defines constants to represent the cell states.
	DEAD_CELL = 0
	LIVE_CELL = 1

	def __init__(self):
		self._elementList = list()


	def minRange(self):
		minim = self._elementList[0]
		# print(minim,"->min")
		for cell in self._elementList:
			if (minim.row > cell.row) and (minim.col > cell.row) and (minim.life == self.LIVE_CELL):
				# print(cell)
				minim = cell
		return (minim.row, minim.col)

	def maxRange(self):
		minim = self._elementList[0]
		# print(minim,"->min")
		for cell in self._elementList:
			if (minim.row < cell.row) and (minim.col < cell.row) and (minim.life == self.LIVE_CELL):
				# print(cell)
				minim = cell
		return (minim.row, minim.col)


	def configure(self, coordList):
		for i in self._elementList:
			i.life = DEAD_CELL

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


	def __getitem__(self, ndxTuple):
		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:
			return self._elementList[ndx]
		return None

	def __setitem__(self, ndxTuple, scalar):
		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:
			if scalar != 0.0:
				self._elementList[ndx].life = scalar
			else:
				self._elementList.pop(ndx)
		else:
			if scalar != 0.0:
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

	grid = SparseLifeGrid()
	grid.configure(INIT_CONFIG)

	print(grid.minRange()," ->min")
	# grid[3,2] = 0
	print(grid.maxRange()," ->max")
