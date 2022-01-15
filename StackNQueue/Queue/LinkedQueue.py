class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link =None


class LinkedQueue:

    def __init__(self):
        self.front=None
        self.rear=None
        self.size_queue=0

    def is_empty(self):

        return self.size_queue==None


    def size(self):
        return self.size_queue



    def enqueue(self,data):
        temp=Node(data)

        if self.front==None:
            self.front=temp
        else:
            self.rear.link = temp
        self.rear=temp
        self.size_queue+=1


    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("The Queue is empty")

        x=self.front.info

        self.front=self.front.link
        self.size_queue-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("The Queue is empty")

        return self.front.info

    def display(self):
        if self.is_empty():
            print("QUeue is empty")
            return
        print("Queue is .... ")
        p=self.front
        while p is not None:
            print(p.info ," --> ",end='')
            p=p.link
        print("None")




linked_queue=LinkedQueue()

linked_queue.enqueue(4)
linked_queue.enqueue(8)
linked_queue.enqueue(16)
linked_queue.enqueue(20)
print(linked_queue.peek())
linked_queue.enqueue(24)
linked_queue.enqueue(28)
linked_queue.display()
print(linked_queue.dequeue())
linked_queue.display()






