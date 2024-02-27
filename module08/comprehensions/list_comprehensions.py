# list/set/dict/tuple comprehensions


res = [1, 2, 3, 4, 5, 6]

for i in range(100):
    if i % 2 == 1:
        res.append(i)
    else:
        res.append(1)
    print(res)
    
    #
    
    # [ <res>  <iterate> <condition>]
    
res = [ i if i % 2 == 1 else 0 for i in range(100)]
print(res)
    
    
    
fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
    
    # Example for loop solution to add 1 to each number in the list
    
number_plus_one = []
for number in numbers:
        number_plus_one.append(number +1)
        
# Example of using a list comprehension to create a list of the numbers plus one.
        numbers_plus_one = [number + 1 for number in numbers]
        number.from_bytes()

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
    
# Rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]


uppercased_fruits = [s.upper() for s in fruits]


# Create a variable named capitalized_fruits 
# and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
# 

capitalized_fruits = [f.capitalize() for f in fruits]
