import re

sample_text = "Alise lives in 1230 First St., Ocean, MD 156789"


res = re.search(r"[0-9]+", sample_text)
print(res.group())  # 2030

res = re.findall(r"[0-9]+", sample_text)
print(res)  # ['1230', '156789']
