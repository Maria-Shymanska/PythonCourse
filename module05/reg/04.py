import re

pattern = "[aeiou]+"

res = re.findall(pattern, "sdsadsadsaeeeddsasa")
print(res)
