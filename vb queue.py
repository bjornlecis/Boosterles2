import queue
q1 = queue.LifoQueue(3)
q1.put(8)
q1.put(5)
q1.put(3)
for i in range(q1.maxsize):
   print(q1.get())

