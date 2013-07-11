import Queue

q1 = Queue.Queue()

for i in range(5):
    q1.put(i)

while not q1.empty():
    print q1.get()
    

q2 = Queue.LifoQueue()

for i in range(5):
    q2.put(i)

while not q2.empty():
    print q2.get()

