n = int(input('Total numbers:'))           
arr = []    
for i in range(n):         
    if i==0:               
        a = 0
    elif i==1:             
        a = 1
        arr = [0, 1]       
    else:                  
        a = arr[0] + arr[1]
        del arr[0]         
        arr.append(a)      
    print(a, end=',')