# __new__   __init__

class Foo:   # class Foo(object)
    def __new__(cls, *args):
        print("Method new Foo")
        print(args)
        instance = super(Foo, cls).__new__(cls)
        return instance
    
    def __init__(self, value) -> None:
        print("Konstructor Foo")
        self.value = value
        
baz = Foo(10)  # __new__() -> __init__()
bar = Foo(20)

print(baz.value, bar.value)
print(baz, bar)