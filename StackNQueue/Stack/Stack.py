class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
        self.stack=[]

    def is_empty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty :(")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty :(")
        return self.stack[-1]

    def display(self):
        print(self.stack)





our_stack=Stack()
print(our_stack.is_empty())
# our_stack.peek()
our_stack.push(2)
our_stack.push(3)
print(our_stack.peek())
our_stack.push(4)
our_stack.push(5)
our_stack.display()
our_stack.pop()
print(our_stack.peek())
our_stack.display()
print(our_stack.is_empty())
