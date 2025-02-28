text = input('Input string：') 
repeat = []                            
not_repeat = []                        
for i in text:                         
    a = text.count(i, 0, len(text))    
    if a>1 and i not in repeat:        
        repeat.append(i)               
    if a == 1 and i not in not_repeat:  
      not_repeat.append(i)             

print(repeat)
print(not_repeat)