from arrayClass import Array
import random

class RGBColor:
	def __init__(self, red =0, green = 0, blue=0):
		self.red = red
		self.green = green
		self.blue = blue

	def __repr__(self):
		return f"({self.red}, {self.green}, {self.blue})"

	def RGB(self):
		return (self.red, self.green, self.blue)

# gray = round( 0.299 * R + 0.587 * G + 0.114 * B )
	def Grey(self):
		return round(0.299 * self.red + 0.587 * self.green + 0.114 * self.blue)

class ColorImage:
	def __init__(self, nrows, ncols):
		self._nrows = nrows
		self._ncols = ncols
		self._size = self._ncols * self._nrows
		self._pixelsArray = Array(self._size)


	def width(self):
		return self._ncols

	def height(self):
		return self._nrows 

	def clear(self,color):
		assert 0 <= color.red <= 255 and 0 <= color.blue <= 255 and  0<= color.green <=255,"Object has to be color <RGB>"
		self._pixelsArray.clear(color)

	def ImageNoise(self):
		for i in range(self._size):
			self._pixelsArray[i] = RGBColor(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

	def Image(self):
		for i in range(self._nrows):
			for j in range(self._ncols):
				print(self._pixelsArray[self._computeIndex((i,j))].Grey(), end= " ")
			print("")
		print("_" * 50)

	def __getitem__(self,  ndxTuple):
		assert ndxTuple[0] < self._nrows and ndxTuple[1] < self._ncols, "Out of range"
		return self._pixelsArray[self._computeIndex(ndxTuple)]

	def __setitem__(self, ndxTuple, value):

		self._pixelsArray[self._computeIndex(ndxTuple)] = value

	def _computeIndex(self,idx):
		return idx[0] * self._nrows + idx[1]

if __name__ == '__main__':
	first= ColorImage(10,10)
	color = RGBColor(255,23,10)
	first.clear(color)
	first.ImageNoise()
	first.Image()
