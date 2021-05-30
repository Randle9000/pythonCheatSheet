class SequenceGenerator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._sequence):
            return self._sequence[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        pass

a = [1,2,3,4]
print(a)
try:
    print(next(a))
except TypeError as e:
    pass

sga = SequenceGenerator(a)
while True:
    try:
        print(next(sga))
    except StopIteration as e:
        break