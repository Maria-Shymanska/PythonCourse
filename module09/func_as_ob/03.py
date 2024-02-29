# Function as a first class object
# Function can be returned as a result of another function


def mul(a, b):
    return a * b

def add(a, b):
    return (a + b)


def ops(operator):
    if operator == "*":
        return mul
    elif operator == "+":
        return add
    else:
        raise ValueError ("operator not supported")
    
f = ops("*")
res = f(2,3)
print (res)

