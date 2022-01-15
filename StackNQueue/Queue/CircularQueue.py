class EmptyQueueError(Exception):
    pass

class CircularQueue:

    def __init__(self,default_size=10):
        self.queue=[None]*default_size
        self.front=0
        self.count=0

    def is_empty(self):
        return self.count==0

    def size(self):
        return self.count

    def enqueue(self,item):

        if self.count==len(self.queue):
            self.resize(2*len(self.queue))
        i=(self.front+self.count)%len(self.queue)

        self.queue[i]=item
        self.count+=1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x=self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1)%len(self.queue)
        self.count-=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self.queue[self.front]

    def display(self):
        print(self.queue)

    def resize(self,newsize):
        old_list=self.queue
        self.queue=[None]*newsize
        i=self.front
        for j in range(self.count):
            self.queue[j]=old_list[i]
            i=(1+i)%len(old_list)
        self.front=0



circular_queue=CircularQueue(8)
print(circular_queue.is_empty())
# circular_queue.peek()
circular_queue.enqueue(2)
circular_queue.enqueue(3)
circular_queue.enqueue(4)
circular_queue.enqueue(5)
circular_queue.display()
print(circular_queue.peek())
circular_queue.enqueue(10)
circular_queue.enqueue(12)
circular_queue.enqueue(15)
circular_queue.enqueue(25)
circular_queue.display()
circular_queue.enqueue(50)
circular_queue.dequeue()
print(circular_queue.peek())
circular_queue.display()






