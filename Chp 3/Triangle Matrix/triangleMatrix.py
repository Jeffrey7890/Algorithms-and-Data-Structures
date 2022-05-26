
from arrayClass import Array

class TriangleArray:
	def __init__(self, n_row, n_cols):
		assert n_row == n_cols, "This must be a square Matrix"
		self.n_cols = n_cols
		self.n_row = n_row
		size = 0
		for i in range(1, n_row+1):
			size+=i

		self._elements = Array(size)

	def clear(self, value):
		self._elements.clear(value)

	# Column-major order
	def _computeIndex(self, idx):
		offset  = 0
		i = idx[0]
		N = i + 1
		j = idx[1]

		assert 1 <= i+1 and j+1 <= N and i+1 >= j+1, "Out of range!"
		return N + (i * (i - 1))//2 + j - 1
		 

	def __getitem__(self, ndxTuple):
		return self._elements[self._computeIndex(ndxTuple)]

	def __setitem__(self, ndxTuple, value):
		self._elements[self._computeIndex(ndxTuple)] = value

	def __repr__(self):
		for i in range(self.n_row):
			for j in range(i+1):
				print(self._elements[self._computeIndex((i,j))],end = " ")
			print(" ")
		return "<Triangle Matrix class>"

	def __iter__(self):
		return _TriangleIterator(self._elements)

class _TriangleIterator:
	def __init__(self, triangleRef):
		self.triangleRef = triangleRef
		self._curNdx = 0

	def __next__(self):
		if self._curNdx < len(self.triangleRef):
			entry = self.triangleRef[self._curNdx]
			self._curNdx+=1
			return entry
		else:
			raise StopIteration

	


if __name__ == '__main__':
	tetris = TriangleArray(4,4)
	tetris.clear("*")
	print(tetris)
	for i in tetris:
		print(i, end = " ")