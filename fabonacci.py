x=1
a=0
while x<4000000:
    sum=x+a
    a=x
    x=sum
    print(sum)
