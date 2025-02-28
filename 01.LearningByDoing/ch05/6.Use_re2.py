import re

m = re.search(r's[a-z]+e', 'thisstest')
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())