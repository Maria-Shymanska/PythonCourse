from collections import UserList
from random import randint


class MyList(UserList):
    _info = "list class !!!"
    
    def get_positive(self):
        return list(filter(lambda x: x >= 0, self.data))
    
    def get_negative(self):
        return list(filter(lambda x: x < 0, self.data))
    
    def info(self):
        return self.info
    
result = []
for _ in range(0, 20):
    result.append(randint(-5, 5))      # Generation of a random number within a given range
results = MyList(result)  # results = []

print(results)
print(results.get_positive())
print(results.get_negative())
print(results.info())
print(MyList.__mro__)
results.sort()
print(results)

