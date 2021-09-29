from fractions import Fraction


class RationRange:
    def __init__(self, start, stop, num_steps):
        if num_steps != int(num_steps):
            raise ValueError(f"num_steps: {num_steps} is not integer")
        if num_steps < 1:
            raise ValueError(f"num_steps: {num_steps} is not positive")
        self._start = Fraction(start)
        self._num_steps = num_steps
        self._step = Fraction(stop - start, num_steps)
        self._index = 0

    def __next__(self):
        if self._index > self._num_steps:
            raise StopIteration
        result = self._start + self._step * self._index
        self._index += 1
        return result

    def __iter__(self):
        return self

iterator = RationRange(1,3,7)

print([float(x) for x in iterator])
next(iterator)