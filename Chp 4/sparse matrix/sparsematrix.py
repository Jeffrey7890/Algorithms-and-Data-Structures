

# Implementation of the sparse Matrix ADT using a list.

class SparseMatrix:

	def __init__(self, numRows, numCols):
		self._numRows = numRows
		self._numCols = numCols
		self._elementList = list()

	def numRows(self):
		return self._numRows


	def numCols(self):
		return self._numCols


	def __getitem__(self, ndxTuple):
		return self._elementList[self._findPosition(ndxTuple[0], ndxTuple[1])]

	def __setitem__(self, ndxTuple, scalar):
		ndx = self._findPosition(ndxTuple[0], ndxTuple[1])
		if ndx is not None:
			if scalar != 0.0:
				self._elementList[ndx].value = scalar
			else:
				self._elementList.pop(ndx)
		else:
			if scalar != 0.0:
				element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
				self._elementList.append(element)

	def __add__(self, rhsMatrix):
		assert rhsMatrix.numRows() == self.numRows() and \
			rhsMatrix.numCols() == self.numCols(),\
			"Matrix sizes not compatible for the add operation."

		newMatrix = SparseMatrix(self.numRows(), self.numCols())

		for element in self._elementList:
			dupElement = _MatrixElement(element.row, element.col, element.value)
			newMatrix._elementList.append(dupElement)

		for element in rhsMatrix._elementList:
			value = newMatrix[element.row, element.col]
			value += element.value

			newMatrix[element.row, element.col] = value 

		return newMatrix


	def __mul__(self, rhsMatrix):
		pass

	def __sub__(self, rhsMatrix):
		pass 

	 
	def scaleBy(self, scalar):
		for element in self._elementList:
			element.value *= scalar

	def _findPosition(self, row, col):
		n = len(self._elementList)
		for i in range(n):
			if row == self._elementList[i].row and col == self._elementList[i].col:
				return i 
		return None


class _MatrixElement:
	def __init__(self, row, col, value):
		self.row = row
		self.col = col 
		self.value = value