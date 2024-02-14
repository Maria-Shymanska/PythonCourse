import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o first_last@iana.org first_middle@iana.org abc111@test.com.net"

# uppercase

pattern = r"\b[A-Z]{1}[\w\.]"
res = re.findall(pattern, text)
print(res)