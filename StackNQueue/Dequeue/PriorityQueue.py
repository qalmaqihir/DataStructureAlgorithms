class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self,value,pr):
        self.info=value
        self.priority=pr
        self.link=None

class PriorityQueue:
    def __init__(self):
        self.front=None

    def enqueue(self,data, data_priority):
        temp=Node(data, data_priority)

        # if queue is empty or element to be added has higher p than first element --> add item to the start
        if self.is_empty() or data_priority>self.front.priority:
            temp.link = self.front
            self.front=temp

        else:
            p=self.front
            while p.link != None and p.link.priority <= data_priority:
                p=p.link
            temp.link = p.link
            p.link=temp

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("P. Dequeue is Empty.., ")
        x=self.front.info
        self.front=self.front.link

        return x

    def is_empty(self):
        return self.front==None

    def display(self):
        if self.is_empty():
            raise EmptyQueueError("P. Dequeue is Empty.., ")
        print("Priority Queue is ...")
        print("Item \t Priority")
        p=self.front
        while p is not None:
            print(p.info, "---> ",p.priority)
            p=p.link

        print("None")



pdq=PriorityQueue()
pdq.enqueue(34,2)
pdq.enqueue(32,1)
pdq.enqueue(30,3)
pdq.enqueue(30,1)
pdq.enqueue(38,4)
pdq.display()
pdq.enqueue(39,9)
pdq.display()