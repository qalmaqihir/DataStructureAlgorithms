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

    def insert_after(self,data,x):
        temp=Node(data)
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        if p is None:
            print(x, " Not present in the list")
        else:
            temp.link=p.link
            p.link=temp

    def insert_before(self,data,x):
        # if the list is empty
        if self.start is None:
            print("List is empty")
            return
        # if x is the first node in the list
        if x==self.start.info:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return
        # Find the precedant node to x
        p = self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link

        if p.link is None:
            print(x, " Not present in the list")
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp

    def insert_at_position(self,data,k):
        # if the data is to be inserted in the start  of the list

        if k==1:
            temp=Node(data)
            temp.link=self.start
            self.start=temp
            return
        p=self.start
        i=1
        while i<k-1 and p is not None: # find a reference to k-1 node
            p=p.link
            i+=1
        if p in None:
            print("You can insert up to the position ",i)
        else:
            temp=Node(data)
            temp.link=p.link
            p.link=temp
            return


    def delete_first_node(self):
        if self.start is None:
            return

        self.start=self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start=None
        p=self.start
        while p.link.link is not None:
            p=p.link
        p.link=None

    def delete_node(self,x):

        if self.start is None:
            print("List is empty")
            return
        # deletion of the first node
        if self.start.info ==x:
            self.start = self.start.link

        p=self.start
        while p.link is not None:
           if  p.link.info==x:
               break
           p=p.link
        if p.link is None:
            print(x, " is not in the list")
        else:
            p.link=p.link.link

    def reverse_list(self):
        prev=None
        p=self.start
        while p is not None:
            next= p.link
            p.link=prev
            prev=p
            p=next
        self.start=prev

    def bubble_sort_exdata(self):
        end=None
        while end!=self.start.link:
            p=self.start
            while p.link !=end:
                q=p.link
                if p.info>q.info:
                    q.info,p.info=p.info, q.info
                p=p.link
            end=p

    def bubble_sort_exlinks(self):
        end = None
        while end!=self.start.link:
            r=p=self.start
            while p.link!=end:
                q=p.link
                if p.info>q.info:
                    p.link=q.link
                    p.link=p
                    if p!=self.start:
                        r.link=q
                    else:
                        self.start=q
                    p,q=q,p
                r=p
                p=p.link
            end=p










listt= SingalLinkedList()

# print(listt.display_list())
# print(listt.search(8))
# print(listt.count_nodes())

listt.create_list()
listt.display_list()
# listt.insert_at_end(-1)
# listt.insert_in_beginning(0)
# listt.search(-2)
# listt.count_nodes()
# listt.display_list()
# listt.insert_after()
# listt.insert_after(-1,0)
# listt.display_list()
# listt.insert_before(3,5)
# listt.display_list()

listt.reverse_list()
print("revered List \n")
listt.display_list()