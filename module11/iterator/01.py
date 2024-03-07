from random import randint

class RandIterator:
    def __init__(self, start, end, quantity) -> None:
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0
        
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)
        
my_random_list = RandIterator(1, 20, 3)
for rn in my_random_list:
    print(rn, end=" ")