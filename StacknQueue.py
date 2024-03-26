# Stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
print(stack)

# Queue
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.popleft()
print(queue)
