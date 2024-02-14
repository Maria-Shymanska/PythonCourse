import re

text = "news/2023/12/31"

pattern = "\w+/\d{4}/\d{2}/\d{2}"

# non-capturing groups, groups()

res = re.findall(pattern, text)

print(res)
