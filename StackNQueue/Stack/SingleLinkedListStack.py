'''
We take the beginning of the single linked list as the top of the stack to have push -> O(1) and pop ->O(1)
if we take the end of single linked list the push and pop will be O(n)
'''

class EmptyStackError(Exception):
    pass

class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class SingleLinkedListStack:
    def __init__(self):
        self.top=None

    def is_empty(self):
        return self.top==None

    def size(self):
        if self.top is None:
            return 0
        count=0
        p=self.top

        while p is not None:
            count+=1
            p=p.link
        return count

    def push(self,x):
        temp=Node(x)

        temp.link=self.top
        self.top=temp

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("No item to pop :(")
        popped=self.top.info
        self.top=self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is Empty. No item to peek :(")
        return self.top.info

    def display(self):
        if self.is_empty():
            raise EmptyStackError("Stack is Empty. Nothing to display :(")

        print("Stack is ...")

        p=self.top
        while p is not None:
            print(p.info,"--> ",end='')
            p=p.link
        print("None")



our_stack = SingleLinkedListStack()

# our_stack.peek()
print(our_stack.is_empty())
our_stack.push(2)
our_stack.push(4)
our_stack.push(16)
print(our_stack.peek())
our_stack.push(196)
our_stack.push(0)
print("size is: ", our_stack.size())
our_stack.display()
our_stack.pop()
our_stack.display()
our_stack.pop()
our_stack.display()
print("size is: ",our_stack.size())
