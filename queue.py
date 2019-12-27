from collections import deque
queue = deque(list(range(10, 20, 2)))
# queue.append(1)
# queue.append(2)
# queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("no items left")
else:
    queue.popleft()
print(queue)
