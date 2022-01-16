class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link =None


class CircularLinkedQueue:
    def __init__(self):
        self.rear=None

    def is_empty(self):
        return self.rear==None

    def size(self):
        if self.is_empty():
            return 0

        n=0
        p=self.rear.link
        while True:
            n+=1
            p=p.link
            if p==self.rear.link:
                break

        return n

    def enqueue(self,data):
        temp =Node(data)

        if self.is_empty():
            self.rear=temp
            temp=self.rear.link

        else:
            temp.link =self.rear.link
            self.rear.link=temp
            self.rear=temp
    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        if self.rear.link == self.rear: # List has only one node
            temp=self.rear
            self.rear=None

        else:
            temp = self.rear.link
            self.rear.link=self.rear.link.link
        return temp.info

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Nothing to Peek...")

        return self.rear.link.info

    def display(self):
        if self.is_empty():
            print("list is empty")
            return
        p=self.rear.link
        while True:
            print(p.info," --> ",end='')
            p=p.link
            if p==self.rear.link:
                break

        print("None")




qu = CircularLinkedQueue()
qu.enqueue(4)
qu.enqueue(3)
qu.enqueue(2)
qu.enqueue(1)
# qu.display()

qu.dequeue()