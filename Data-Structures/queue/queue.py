class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty!")

    def __len__(self):
        return len(self.queue)

    def __repr__(self):
        return f"{self.queue}"

    def __str__(self):
        return f"{self.queue}"
        

# testing
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"q: {q}")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
