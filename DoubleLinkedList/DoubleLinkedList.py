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

    def delete_first_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        self.start=self.start.next
        self.start.prev=None

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start=None
            return
        p=self.start
        while p.next !=None:
            p=p.next
        p.prev.next=None

    def delete_node(self,x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start=None
            else:
                print(x,' not present in the list')
            return
        # deletion of the first node
        if self.start.info ==x:
            self.start =self.start.next
            self.start.prev= None
            return

        p = self.start
        while p.next is not None:
            if p.info ==x:
                break
            p=p.next
        if p.next is not None:# node to be deleted is in between
            p.prev.next=p.next
            p.next.prev=None
        else: # p refers to last node
            if p.info==x:
                p.prev.next=None
            else:
                print(x," Not present in the list")

    def reverse_list(self):
        if self.start is None:
            return

        p1=self.start
        p2=p1.next
        p1.next=None
        p1.prev=p2

        while p2 is not None:
            p2.prev = p2.next
            p2.next=p1
            p1=p2
            p2=p2.prev
        self.start=p1







listt=DoubleLinkedList()
listt.display_list()
listt.create_list()
listt.insert_before_self(5)
listt.insert_at_end(-1)
listt.insert_at_beginning(0)
listt.display_list()
listt.insert_after(-4)
listt.display_list()