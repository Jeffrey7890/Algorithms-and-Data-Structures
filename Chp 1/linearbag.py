# An iterator for the Bag ADT implemented as a Python list.
class _BagIterator:
	def __init__(self, theList):
		self._bagItems = theList
		self._curItem = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._curItem<len(self._bagItems):
			item = self._bagItems[self._curItem]
			self._curItem +=1
			return item
		else:
			raise StopIteration



# Implements the Bag ADT container using a python List.
class Bag:
	# Constructs and empty bag.
	def __init__(self):
		self._theItems = list()

	# Returns the number of items in the bag.
	def __len__(self):
		return len(self._theItems)

	# Determines if an items is contained in the bag.
	def __contains__(self, item):
		return item in self._theItems

	# Add a new item to the bag.
	def add(self, item):
		return self._theItems.append(item)

	# Removes and returns an instance of the item from the bag.
	def remove(self, item):
		assert item in self._theItems, "The item must be in the bag."
		ndx = self._theItems.index(item)
		return self._theItems.pop(ndx)

	# Returns an iterator for traversing the list of items.
	def __iter__(self, item):
		return _BagIterator(self._theItems)

