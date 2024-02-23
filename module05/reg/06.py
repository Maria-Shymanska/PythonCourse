import re


# multiline string

string = "abc 12\    de 23\     f45    \n 6"

res = re.sub(r"\s+", "", string)

print(res)
