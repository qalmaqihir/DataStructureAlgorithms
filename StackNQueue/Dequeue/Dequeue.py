class EmptyQueueError(Exception):
    pass

class Dequeu:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def insert_front(self,item):
        self.items.insert(0,item)

    def insert_rear(self,item):
        self.items.append(item)

    def delete_font(self):
        return self.items.pop(0)

    def delete_rear(self):
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Dequeue is empty...")
        return self.items[0]

    def end(self):
        if self.is_empty():
            raise EmptyQueueError("Dequeue is empty...")
        return self.items[-1]


    def display(self):
        print(self.items)




dequeue=Dequeu()

dequeue.insert_front(0)
dequeue.insert_front(2)
dequeue.insert_front(4)
dequeue.insert_rear(9)
dequeue.is_empty()
dequeue.display()
dequeue.delete_rear()
dequeue.display()
dequeue.insert_rear(-2)
dequeue.insert_rear(-3)
dequeue.insert_rear(-4)
dequeue.delete_font()
dequeue.display()



