
def mul(a, b):
    return a * b

def add(*args):
    res = 0
    for i in args:
        res += i
        return res
    
def ops(operator):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        raise ValueError ("operator not supported")
    
res = ops('+')()() # carring
print (res) 