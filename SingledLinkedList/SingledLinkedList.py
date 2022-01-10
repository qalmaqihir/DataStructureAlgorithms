class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class SingalLinkedList:
    def __init__(self):
        self.start=None

    def display_list(self):
        if self.start is None:
            print("List is empty")
        else:
            print("List is ...")
            p=self.start
            while p is not None:
                print(p.info, " ", end="")
                p=p.link
            print()

    def count_nodes(self):
        if self.start is None:
            print("List has no nodes")
        else:
            p=self.start
            n=0
            while p is not None:
                p=p.link
                n+=1
            print("Number of nodes in the list is = ",n)

    def search(self,x):
        p=self.start
        position=1
        while p is not None:
            if p.info ==x:
                print(x, " is at postion: ", position)
                return True
            position+=1
            p=p.link

        print(x," is not in the list..")
        return False

    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.link = self.start
        self.start=temp

    def insert_at_end(self,data):
        temp = Node(data)
        if self.start is None:
            self.start=temp
            return

        p = self.start
        while p.link is not None:
            p=p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n==0:
            return
        for i in range(n):
            data = int(input("Enter the element to be insearted: "))
            self.insert_at_end(data)








listt= SingalLinkedList()

# print(listt.display_list())
# print(listt.search(8))
# print(listt.count_nodes())

listt.create_list()
listt.display_list()
listt.insert_at_end(-1)
listt.insert_in_beginning(0)
listt.search(-2)
listt.count_nodes()
listt.display_list()
