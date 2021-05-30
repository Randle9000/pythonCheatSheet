import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push('foo', 1)
q.push('bar', 5)
q.push('spam', 4)
q.push(1, 1)

print(len(q._queue))

while len(q._queue) > 0 :
    print(q.pop())

# print("Should be bar:", q.pop())
# print(len(q._queue))
#
# print("Should be spam:", q.pop())
# print("Should be foo:", q.pop())
# print("Should be grok:", q.pop())
