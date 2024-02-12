
# args = tuple arguments
# kwargs = dict keyword arguments

def add(a, b, *args):
    res = a + b
    for number in args:
        res += number


    return res


result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15 (1 + 2 + 3 + 4 + 5)



def intro(firstname, *args, **kwargs):
    print(args)
    print(kwargs)
    
    print("firstname", firstname)
    
    for key, value in kwargs.items():
        print(key, value)



intro("Oleksandr",  "12312", True, 1231, last_name="Holodetskyi", age = 18, school="GoIT",)


def my_sum(*args):
    result = 0
    for x in args:
        result += x
        return result
    
    
list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))












