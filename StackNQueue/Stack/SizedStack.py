class StackEmptyError(Exception):
    pass

class StackFullError(Exception):
    pass

class SizedStack:
    def __init__(self,max_size=10):
        self.stack=[None]*max_size
        self.count=0

    def size(self):
        return self.count

    def isFull(self):
        return self.count==len(self.stack)

    def is_empty(self):
        return self.count==0

    def push(self,x):
        if self.isFull():
            raise StackFullError("Stack is full, cant push more items :(")
        self.stack[self.count]=x
        self.count+=1

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty, can't pop :(")
        x=self.stack[self.count-1]

        self.stack[self.count-1]=None
        self.count+1

    def peek(self):
        if self.is_empty():
            raise StackEmptyError(" NOTHING  to peek, Stack is empty :(")
        return self.stack[self.count-1]

    def display(self):
        print(self.stack)




our_stack = SizedStack(8)

print(our_stack.isFull())
our_stack.push(3)
our_stack.push(6)
our_stack.push(9)
our_stack.push(12)
our_stack.display()
our_stack.pop()
our_stack.push(15)
our_stack.display()
print(our_stack.peek())
# our_stack.pop()
# our_stack.display()