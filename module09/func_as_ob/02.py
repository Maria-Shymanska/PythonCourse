# Function as a first class object
# pass function as an argument to another function


def mul(a, b):
    return a * b

def add(a, b):
    return (a + b)


def ops(a, b, func):
    res = func (a, b)
    
    return res

res = ops(2, 3, mul)
print(res)
res = ops(2, 3, add)
print(res)


