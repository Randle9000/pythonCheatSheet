from typing import Sequence, Any
from collections.abc import Iterable

expr_tree = "* + - a b c d".split(' ')
iterator = iter(expr_tree)


class LevelOrderIterator:

    def __init__(self, seq: Sequence):
        self._seq = seq
        self._index = 0

    def __next__(self) -> Any:
        if self._index >= len(self._seq):
            raise StopIteration
        result = self._seq[self._index]
        self._index += 1
        return result

    def __iter__(self):
        return self


iterator = LevelOrderIterator(expr_tree)
print(next(iterator))
print(next(iterator))

for x in iterator: # it takes t
    print(x)

iterator = LevelOrderIterator(expr_tree)
print(" ".join(iterator))


