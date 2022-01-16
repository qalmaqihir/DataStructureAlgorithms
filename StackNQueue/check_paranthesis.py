from StackNQueue import Stack

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
                index+=1
    if balanced and s.is_empty():
        return True
    else:
        return False



par_check("(()())")# True

