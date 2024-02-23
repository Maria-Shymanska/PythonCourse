# list/set/dict/tuple comprehensions


res = [1, 2, 3, 4, 5, 6]

for i in range(100):
    if i % 2 == 1:
        res.append(i)
    else:
        res.append(0)
    print(res)
    
    ###
    
    # [ <res>  <iterate> <condition>]
    
    res = [ i if i % 2 == 1 else 0 for i in range(100)]
    print(res)