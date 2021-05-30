from collections import deque
deque_holder = deque(maxlen=4)


for i in range(10):
    deque_holder.append(i)
    if len(deque_holder) >= 3:
        print(deque_holder)