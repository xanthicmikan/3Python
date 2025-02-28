import random
a = []
while len(a)<6:
    b=random.randint(1,49)
    if b not in a:
        a.append(b)
print(a)