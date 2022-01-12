class Node(object):
    def __init__(self,value):
        self.info=value
        self.prev=None
        self.next=None

class DoubleLinkedList(object):
    def __init__(self):
        self.start=None

    def create_list(self):
        n=int(input("Enter the number of nodes: "))
        if n==0:
            print("No Nodes no list:(")
            return
        data = int(input("Enter the first element to be inserted: "))
        self.insert_at_end(data)
        for i in range(n-1):
            data=int(input("Enter the next element: "))
            self.insert_at_end(data)


    def display_list(self):
        if self.start is None:
            print("List is empty")
            return

        print("list is ... ")
        p=self.start
        while p is not None:
            print(p.info, " ", end='')
            p=p.next
        print()
        return

    def insert_at_beginning(self,x):
        temp = Node(x)
        if self.start is None:
            self.start=temp
        else:
            temp.next = self.start
            self.start.prev=temp
            self.start=temp


    def insert_at_end(self,x):
        temp= Node(x)
        p=self.start
        while p.next is not None:
            p=p.next

        p.next=temp
        temp.prev=p

    def insert_after(self,data,x):
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info ==x:
                break
            p=p.next
        if p is None:
            print(x, " not present in the list")
        else:
            temp.prev=p
            temp.next=p.next
            if p.next is not None:      # should not be done if p refers to last Node
                p.next.prev=temp
            p.next=temp;


    def insert_after_self(self,data,x):
        temp = Node(data)
        p=self.start
        while p is not None:
            if p.info==x:
                temp.prev=p
                temp.next=p.next
                p.next.prev = temp
                p.next = temp
                return
            p=p.next
        print("given node : ", x, " is not in the list")
        return


    def insert_before(self,data,x):
        temp = Node(data)
        if self.start is None:
            print("List is empty")
            return
        if self.start.info==x:
            temp.next=self.start
            self.start.prev=temp
            self.start=temp
            return

        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.next

        if p is None:
            print(x, " not in the list")
        else:
            temp.prev=p.prev
            temp.next=p
            p.prev.next=temp
            p.prev=temp




    def insert_before_self(self, data,x):
        p= self.start
        while p is not None:
            if p.next == data:
                temp = Node(x)
                temp.prev = p.next
                temp.next = p
                p.prev.next= temp
                p.prev = temp
                return
            p = p.next
        print("given node : ", x, " is not in the list")






listt=DoubleLinkedList()
listt.display_list()
listt.create_list()
listt.insert_before_self(5)
listt.insert_at_end(-1)
listt.insert_at_beginning(0)
listt.display_list()
listt.insert_after(-4)
listt.display_list()