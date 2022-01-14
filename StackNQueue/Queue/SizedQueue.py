'''
Insertion --> Enqueue performed at the rear (end)
Deletion --> Dequeue performed at the front
'''

class EmptyQueueError(Exception):
    pass

class QueueImporved:
    def __init__(self):
        self.queue=[]
        self.front=0

    def is_empty(self):
        return self.front==len(self.queue)

    def size(self):
        return len(self.queue)-self.front

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, can't remove any item :(")

        # Impoved version, where not all the items in the list have to shift
        x=self.queue[self.front]
        self.queue[self.front]=None
        self.front=self.front+1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, Nothing to show:(")

        return self.queue[self.front]

    def display(self):
        print(self.queue)







our_queue=QueueImporved()

print(our_queue.is_empty())
our_queue.enqueue(4)
our_queue.enqueue(41)
our_queue.enqueue(40)
print("Peeking ", our_queue.peek())
our_queue.enqueue(14)
our_queue.display()
print("Peeking ", our_queue.peek())
print(our_queue.dequeue())
our_queue.display()
print(our_queue.dequeue())
our_queue.display()
our_queue.enqueue(0)
our_queue.display()
our_queue.enqueue(1)
our_queue.display()
print(our_queue.size())
print("Peeking ", our_queue.peek())