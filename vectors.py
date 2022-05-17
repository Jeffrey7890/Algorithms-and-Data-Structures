# Implements the Vector ADT using array class.

from arrayClass import Array

class Vector:
    # Creates a new empty vector with an initial capacity of two elements.
    def __init__(self, size = 2):
        self._elements = Array(size)
        self._size = size

    # Returns number of items contained in the vector
    def __len__(self):
        items = 0
        for i in range(self._size):
            if self._elements[i] != None:
                items += 1
        return items

    # Determines if the given item is contained in the vector
    def __contains__(self, item):
        for i in range(self._size):
            if item == self._elements[i]:
                return True
        return False

    # Sets the element at position ndx to contain the given item.
    def __setitem__(self, ndx, item):
        self._elements[ndx] = item
    
    # Returns the item stored in the ndx element of the list.
    def __getitem__(self, ndx):
        return self._elements[ndx]

    # displays the elements to the screen
    def display(self):
        for i in range(self._size):
            if self._elements[i] != None:
                print(self._elements[i], end = ', ')
        print("\n")

    # Adds the given item to the end of the list.
    def append(self, item):
        numb = len(self)
        if  self._size > numb:
            self._elements[numb] = item 
        else:
            self._extend()
            self.append(item)

    # Private class function that extends itself.
    def _extend(self):
        temp = self._elements
        self._elements = Array(self._size*2)
        for i in range(self._size):
            self._elements[i] = temp[i]
        self._size *= 2

    # Clears the class to a given value
    def clear(self, value):
        self._elements.clear(value)

    # Inserts the given item in the element at postion ndx.
    def insert(self, ndx, item):
        length = len(self._elements)
        temp = Vector(length)
        for i in range(ndx, length):
            temp.append(self._elements[i])
            self._elements[i] = None 
        
        self.append(item)

        for i in temp:
            self.append(i)

    # Removes and returns the item from the element from the given ndx postion.
    def remove(self, ndx):
        length = len(self._elements)
        temp = Vector(length)
        for i in range(ndx+1, length):
            temp.append(self._elements[i])
            self._elements[i] = None 
        
        self._elements[ndx] = None 

        for i in temp:
            self.append(i)

    # Creates and returns a new vector that contains a 
    # subsequence of the items in the vector.
    def subVector(self, frm, to):
        size = (to - frm) + 1
        result = Vector(size)
        for i in range(frm, to+1):
            result.append(self._elements[i])
        
        return result

    # Returns the index of the vector element containing the given item.
    def indexOf(self,item):
        for i in range(len(self)):
            if item == self._elements[i]:
                return i 
    
    # Extends this vector by appending the entire contens of the otherVector to this vector.
    def extend(self, otherVector):
        temp = self._elements; ndx = 0
        length = len(self)
        l_size = length + len(otherVector)
        
        if l_size > self._size:
            self._size = l_size*2
            self._elements = Array(self._size)

            for i in range(length):
                self._elements[i] = temp[i]
                ndx+=1

        ndx = length
        for i in range(len(otherVector)):
            self._elements[ndx] = otherVector[i]
            ndx += 1

    # Creates and returns an iterator that can be used to traverse 
    # the elements of the vector.
    def __iter__(self):
        return _VectorIterator(self._elements)


#  Vector Iterator class.
class _VectorIterator:
    def __init__(self, theVector):
        self._vectorRef = theVector
        self._curNdx = 0 

    def __next__(self):
        if self._curNdx < len(self._vectorRef):
            entry = self._vectorRef[self._curNdx]
            self._curNdx +=1
            if entry != None:
                return entry
            else:
                raise StopIteration


if __name__ == "__main__":
    vec3 = Vector()
    vec3.append(10)

    print("Vec3 display: ")
    vec3.display()

    vec4 = Vector(10)
    vec4.append(234)
    vec4.append(56)
    vec4.append(400)
    print("vec4 appended values: ")
    vec4.display()

    print("Extended vec3 to vec4: ")
    vec4.extend(vec3)

    vec4.insert(1,9000)
    print("Inserted 9000 at position 1")
    vec4.display()

    vec4.remove(1)
    print("Removed the position 1")
    vec4.display()

    print("Subvector operation:")
    vec4.subVector(1,3).display()

    print("Index of number 400 is: ", vec4.indexOf(400))

    print("Iterating over vec4")
    for i in vec4:
        print(i)