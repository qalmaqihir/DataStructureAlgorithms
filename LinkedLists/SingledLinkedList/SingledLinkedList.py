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

    def merg1(self,list2):
        merge_lsit = SingalLinkedList()
        merge_lsit.start=self._merg1(self.start,list2.start)
        return merge_lsit

    def _merg1(self,p1,p2):
        if p1.info<=p2.info:
            statM=Node(p1.info)
            p1=p1.link
        else:
            statM=Node(p2.info)
            p2=p2.link
        pM=statM

        while p1 is not None and p2 is not None:
            if p1.info<=p1.info:
                pM.link=Node(p1.info)
                p1=p1.link
            else:
                pM.link=Node(p2.info)
                p2=p2.link
            pM=pM.link

        # if second list has finished and elements left in the first list
        while p1 is not None:
            pM.link =Node(p1.info)
            p1=p1.link
            pM=pM.link

        # if first list has finished and elments left in the second
        while p2 is not None:
            pM.link=Node(p2.info)
            p2 = p2.link
            pM=pM.link

        return pM


    '''
    Merging two sorted lists by rearranging links
    '''
    def merg2(self,list2):
        merge_list = SingalLinkedList()
        merge_list._merg2(self.start,list2.start)

        return merge_list

    def _merg2(self,p1,p2):
        if p1.info <=p2.info:
            startM=p1.info
            p1 = p1.link
        else:
            startM = p2.info
            p2 = p2.link
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link=p1
                pM=pM.link
                p1=p1.link

            else:
                pM.link = p2
                pM=pM.link
                p2=p2.link
        if p1 is None:
            pM.link =p2
        else:
            pM.link = p1
        return startM

    def merge_sort(self):
        self.start =self._merge_sort_rec(self.start)

    def _merge_sort_rec(self,list_start):
        # if list is empty or has one element (base case)
        if list_start is None or list_start.link is None:
            return list_start

        # if more than one element
        start1=list_start
        start2=self._divide_list(list_start)
        start1=self._merge_sort_rec(start1)
        start2=self._merge_sort_rec(start2)
        startM=self._merg2((start1,start2))

        return startM

    def _divide_list(self,p):
        q=p.link.link
        while q is not None and q.link is not None:
            p=p.link
            q=q.link.link
        start2=p.link
        p.link=None
        return start2

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        slowR = self.start
        fastR = self.start

        while fastR is not None and fastR.link is not None:
            slowR=slowR.link
            fastR=fastR.link.link

            if slowR==fastR:
                return slowR
        return None


    def remove_cyle(self):
        c=self.find_cycle()
        if c is None:
            return
        print("Node at which cycle is detected is ",c.info)

        p=c
        q=c
        len_cycle=0

        while True:
            len_cycle+=1
            q=q.link
            if p==q:
                break
        print("lenght of cycle is : ", len_cycle)

        len_rem_list =0
        p=self.start

        while p!=q:
            len_rem_list+=1
            p=p.link
            q=q.link

        print("Number of nodes not included in the cycle are : ", len_rem_list)
        lenght_list = len_cycle+len_rem_list
        print("Lenght of the list is : ", lenght_list)

        p = self.start
        for  i in range(lenght_list-1):
            p=p.link
        p.link = None

    def insert_cycle(self,x):
        if self.start is None:
            return
        p=self.start
        px=None
        prev=None

        while p is not None:
            if p.info==x:
                px=p
            prev=p
            p=p.link
        if px is not None:
            prev.link = px
        else:
            print(x," Not present in list ")

    def concatenate(self,list2):
        if self.start is None:
            self.start=list2.start
            return
        if list2.start is None:
            return
        p=self.start
        while p is not None:
            p=p.link
        p.link=list2.start










#
# listt= SingalLinkedList()
#
# # print(listt.display_list())
# # print(listt.search(8))
# # print(listt.count_nodes())
#
# listt.create_list()
# listt.display_list()
# # listt.insert_at_end(-1)
# # listt.insert_in_beginning(0)
# # listt.search(-2)
# # listt.count_nodes()
# # listt.display_list()
# # listt.insert_after()
# # listt.insert_after(-1,0)
# # listt.display_list()
# # listt.insert_before(3,5)
# # listt.display_list()
#
# listt.reverse_list()
# print("revered List \n")
# listt.display_list()

""""
Checking for megering list
"""

list1=SingalLinkedList()
list2=SingalLinkedList()

list1.create_list()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()

print("First List - "); list1.display_list()
print("Second list - ");list2.display_list()

list3=list1.merg1(list2)
print("Merge with 1st method: ");list3.display_list()

print("First List - "); list1.display_list()
print("Second list - ");list2.display_list()

list3=list1.merg2(list2)
print("Merge with 2nd method: ");list3.display_list()
print("First List - "); list1.display_list()
print("Second list - ");list2.display_list()

