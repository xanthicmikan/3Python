a = b = int(input('Input one positive integer：'))
output = ''                           
while True:                           
    for i in range(2,(a+1)):          
        if i==b:                      
            break
        if a%i==0:                    
            output += f'{i}'          
            a = int(a/i)              
            break                     
    if a==1 or a==b:                   
        break
    else:
        output += '*'                 
if b == a and b!= 1:
    print(f'{b} is prime number')              
elif b == 1:
    print(f'{b} int not prime number, and cannot prime factor') 
else:
    print(f'{b}={output}') 
