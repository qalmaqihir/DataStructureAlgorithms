class Node(object):
    def __init__(self,value):
        self.info=value
        self.link=None

class CircularLinkedList(object):
    def __init__(self):
        self.last=None
    def display_list(self):
        if self.last == None:
            print("Empty list")
            return
        p=self.last.link

        print("List is ...")
        while True:
            print(p.info, " ", end='')
            p = p.link
            if p==self.last.link:
                break

        print()

    def insert_in_empty_list(self,x):
        temp=Node(x)
        self.last = temp
        self.last.link = self.last

    def insert_at_beginning(self,x):
        temp=Node(x)
        if self.last is None:
            self.last=temp
            self.last.link=self.last
            return

        temp.link = self.last.link
        self.last.link=temp

    def insert_at_end(self,x):
        temp=Node(x)
        temp.link=self.last.link
        self.last.link = temp
        self.last=temp

    def create_list(self):
        n=int(input("How many nodes: "))
        if n==0:
            return
        data=int(input("Enter the first node:  "))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input("Enter the next node: "))
            self.insert_at_end(data)

    def insert_after(self,data, x):
        p=self.last.link
        while True:
            if p.info==x:
                break
            p=p.link
            if p==self.last.link:
                break
        if p==self.last.link and p.info!= x:
            print(x," not present in the list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
            if p==self.last:
                self.last=temp

    def delete_first(self):
        if self.last is None:
            return
        if self.last.link == self.last:
            self.last=None
            return
        self.last.link=self.last.link.link


    def delete_only_node(self):
        self.last=None

    def delete_from_end(self):
        if self.last is None: #List is empty
            return
        if self.last.link == self.last: # list has only one node
            self.last=None

        p=self.last.link
        while p.link != self.last:
            p=p.link
        p.link=self.last.link
        self.last=p
    def delete_node(self,x):
        if self.last is None:
            return
        if self.last.link is None and self.last.info==x:
            self.last=None
            return
        if self.last.link.info ==x:
            self.last.link=self.last.link.link
            return
        p=self.last.link

        while p.link!=self.last.link:
            if p.link.info==x:
                break
            p=p.link
        if p.link ==self.last.link:
            print(x, " not found in the list")
        else:
            p.plink=p.plink.link
            if self.last.info==x:
                self.last=p

    def concatenate(self,list2):
        if self.last is None:
            self.last=list2.last
            return
        if list2.last is None:
            return
        p=self.last.link
        self.last.link=list2.last.link
        list2.last.link=p
        self.last=list2.last




lsit=CircularLinkedList()
lsit.create_list()
lsit.display_list()
lsit.insert_at_end(-1)
lsit.display_list()
lsit.insert_after(25,5)
lsit.display_list()

