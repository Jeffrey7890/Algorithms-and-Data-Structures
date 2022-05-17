
from Array2D import Array2D

class Matrix:

	def __init__(self, numRows, numCols):
		self._theGrid = Array2D(numRows, numCols)
		self._theGrid.clear(0)

	def numRows(self):
		return self._theGrid.numRows()

	def numCols(self):
		return self._theGrid.numCols()

	def __getitem__(self, ndxTuple):
		return self._theGrid[ndxTuple[0], ndxTuple[1]]

	def __setitem__(self, ndxTuple, scalar):
		self._theGrid[ndxTuple[0], ndxTuple[1]] = scalar

	def __repr__(self):
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				print(self[r,c], end = "\t")
			print("")
		return ""

	def scaleBy(self, scalar):
		for r in range(self.numRows()):
			for c in range(self.numCols()):
				self[r,c] *= scalar


	def transpose(self):
		newMatrix = Matrix(self.numCols(), self.numRows())
		for i in range(self.numCols()):
			for j in range(self.numRows()):
				newMatrix[i,j] = self._theGrid[j, i]

		return newMatrix

	def __add__(self,rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and\
			   rhsMatrix.numCols() == self.numCols(),\
			   "Matrix sizes not compatible for th add operation."

		newMatrix = Matrix(self.numRows(), self.numCols())

		for r in range(self.numRows()):
			for c in range(self.numCols()):
				newMatrix[r,c] = self[r,c] + rhsMatrix[r,c]
		return newMatrix

	def __sub__(self,rhsMatrix):
		assert	 rhsMatrix.numRows() == self.numRows() and\
				rhsMatrix.numCols() == self.numCols(),\
				"Matrix sizes not compatible for sub operation."
		
		newMatrix = Matrix(self.numRows	(), self.numCols())
		for r in range(self.numRows()):
			for c in range(self.numCols	()):
				newMatrix[r,c] = self[r,c] - rhsMatrix[r,c]

		return	newMatrix

	def __mul__(self, rhsMatrix):
		assert rhsMatrix.numCols() == self.numRows(), \
				" Both Matrix must be (M x N) * (N x M)"

		newMatrix = Matrix(self.numRows(), rhsMatrix.numCols())
		sum = 0
		for k in range(rhsMatrix.numCols()):
			for i in range(self.numRows()):
				for j in range(self.numCols()):
					sum += self._theGrid[k, j] * rhsMatrix[j, i]
				newMatrix[k, i] = sum
				sum = 0
		return newMatrix

if __name__ == '__main__':
	first = Matrix(3,2)
	second = Matrix(2,3)
	first[0,0] = 0
	first[0,1] = 1
	first[1,0] = 2
	first[1,1] = 3
	first[2,0] = 4
	first[2,1] = 5


	second[0,0] = 6
	second[0,1] = 7
	second[0,2] = 8
	second[1,0] = 9
	second[1,1] = 1
	second[1,2] = 0


	print(first*second)
	print(first)
	print(first.transpose())
