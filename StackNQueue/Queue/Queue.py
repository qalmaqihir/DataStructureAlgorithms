'''
Insertion --> Enqueue performed at the rear (end)
Deletion --> Dequeue performed at the front
'''

class EmptyQueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, can't remove any item :(")

        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, Nothing to show:(")

        return self.queue[0]

    def display(self):
        print(self.queue)




our_queue=Queue()

print(our_queue.is_empty())
our_queue.enqueue(4)
our_queue.enqueue(41)
our_queue.enqueue(40)
our_queue.enqueue(14)
our_queue.display()
# print(our_queue.peek())
print(our_queue.dequeue())
our_queue.display()
print(our_queue.dequeue())
our_queue.display()
our_queue.enqueue(0)
our_queue.display()
our_queue.enqueue(1)

our_queue.display()
