import re 

res = "I bought 77 nuts for 6$ and 110 bolts for 3$"

r = re.findall(r'\d{1,2}', res)
print(r)

