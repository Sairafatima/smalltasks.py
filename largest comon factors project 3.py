x=600851475143 
a=2
while a<x:
    if x%a==0:
        b=2
        y=True
        while b<a:
            if a%b==0:
                y=False
                break
            else:b+=1
        if y:
            print(a)
    a+=1
        
