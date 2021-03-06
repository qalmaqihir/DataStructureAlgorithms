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





# our_stack=Stack()
# print(our_stack.is_empty())
# # our_stack.peek()
# our_stack.push(2)
# our_stack.push(3)
# print(our_stack.peek())
# our_stack.push(4)
# our_stack.push(5)
# our_stack.display()
# our_stack.pop()
# print(our_stack.peek())
# our_stack.display()
# print(our_stack.is_empty())




def par_check(symbol_string):
    s=Stack()
    balanced=True
    index=0

    while index<len(symbol_string) and balanced:
        symbol=symbol_string[index]
        if  symbol=="(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced=False
            else:
                s.pop()
        index+=1

    if balanced and s.is_empty():
        return True
    else:
        return False



# print(par_check("(()())"))# True
# print(par_check("(()())())(("))


# A General Case for any symbol

def par_checker_general(symbol_string):
    s=Stack()
    balanced=True
    index=0
    while index <len(symbol_string) and balanced:
        symbol=symbol_string[index]

        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced=False
            else:
                top=s.pop()
                if not matches(top,symbol):
                    balanced=False
        index+=1
    if balanced and s.is_empty():
        return  True
    else:
        return False

def matches(open, close):
    open="({["
    close=")}]"
    return open.index(open)==close.index(close)

#
# print(par_checker_general("{{([][])}()}"))
# print(par_checker_general("{}{{()()[][]]}}"))


def base_conversion(dec_num,base):
    digits='0123456789ABCDEF'
    rem_stack=Stack()

    while dec_num>0:
        rem = dec_num%base
        rem_stack.push(rem)
        dec_num=dec_num//base

    new_string=""
    while not rem_stack.is_empty():
        new_string=new_string + digits[rem_stack.pop()]

    return new_string

print(base_conversion(25,2))
print(base_conversion(25,8))
print(base_conversion(25,16))

