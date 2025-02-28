a = input('Input a, b.....:')
b = a.split(',')
output = 0
for i in b:
    output += int(i)

print(f'Sum = {output}')
a = input('end')