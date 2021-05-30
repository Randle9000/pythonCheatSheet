class Vector:
    def __init__(self, length):
        self._coords = [0] * length

    def __len__(self): # len()
        return len(self._coords)

    def __getitem__(self, j): # v[1]
        return self._coords[j]

    def __setitem__(self, j, value): # v[1] = 5
        self._coords[j] = value

    def __add__(self, other): # v1 + v2
        ":return the sum of two vector"
        if len(self) != len(other): # relies on len methods
            raise ValueError('length of vectors must be same')
        result = Vector(len(self))  # len(self) is equal to self.__len__()
        for i in range(len(self)):
            result[i] = self._coords[i] + other[i]
        return result

    def __eq__(self, other): # v1 == v2
        return self._coords == other._coords

    def __ne__(self, other): # v1 != v2
        return not self == other # relies on __eq__ jakie to kurwa mądre!

    def __str__(self):
        return "<" + str(self._coords)[1:] + ">"

v1 = Vector(5)
v1[1] = 5
v1[2] = 3
print(v1)
v2 = Vector(5)
v2[1] = 3
v2[2] = 2
print(v1+v2)








