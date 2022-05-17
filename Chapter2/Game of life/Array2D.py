from arrayClass import Array

class Array2D:
	# Creates a 2-D array of size numRows x numCols.
	def __init__(self, numRows, numCols):
		# Create a 1-D array to store an array reference for each row.
		self._theRows = Array(numRows)

		# Create the 1-D arrays for each row of the 2-D array.
		for i in range(numRows):
			self._theRows[i] = Array(numCols)

	# Returns the number of rows in the 2-D array.
	def numRows(self):
		return len(self._theRows)

	# Returns the number of columns in the 2-D array.
	def numCols(self):
		return len(self._theRows[0])

	# Clears the array by setting every element to the given value.
	def clear(self, value):
		for row in range(self.numRows()):
			self._theRows[row].clear(value)

	# Gets the contents of the element at position[i, j]
	def __getitem__(self, ndxTuple):
		assert len(ndxTuple) == 2, "Invalid number of array subscripts."
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >= 0 and row < self.numRows()\
			and col >= 0 and col < self.numCols(),\
				"Array subscript out of range."
		the1dArray = self._theRows[row]
		return the1dArray[col]

	# Sets the contents of the element at position [i, j] to value.
	def __setitem__(self, ndxTuple, value):
		assert len(ndxTuple) == 2, "Invalid number of array subscripts."
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >= 0 and row < self.numRows()\
			and col >= 0 and col < self.numCols(),\
				"Array subscript out of range."
		the1dArray = self._theRows[row]
		the1dArray[col] = value

if __name__ == "__main__":
	first = Array2D(3,3)