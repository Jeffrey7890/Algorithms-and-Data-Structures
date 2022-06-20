
from sparseLifeGame import SparseLifeGrid
import random

# I was Just trying out a little polymorphism 
# its still needed though

class Grid(SparseLifeGrid):
	def __init__(self, nRow, nCol, INIT_CONFIG):
		super().__init__(nRow, nCol)
		self.configure(INIT_CONFIG)

	def element(self):
		print(self._elementList)


if __name__ == '__main__':
	
	INIT_CONFIG = [(random.randint(0,50-1), random.randint(0,50-1)) for _ in range(400)]
	f = Grid(50,50,INIT_CONFIG)