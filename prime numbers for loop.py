def prime(x):
    a=2
    z=True
    while a<x:
       if x%a==0:
        return False
       
       else:
        a+=1
    if z:
       print(x)
for x in range(1,10000):
   prime(x)
    
    
