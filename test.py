from collections import deque
q = deque()

q.append('a')
q.append('b')
q.append('c')
print("Initial queue:", q)

print("Elements dequeued from the queue:")
print(q.popleft())


print("Queue after removing elements:", q)