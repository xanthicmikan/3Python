def gen(max):                   
    s = set()                  
    for n in range(2,max):     
        if all(n%i>0 for i in s):
            s.add(n)               
            yield n                
print(*gen(100))   