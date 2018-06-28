l=[]
for i in range (0,20):
    x=int(input("ENTER YOUR NUMBER"))
    l.append(x)
for i in l:
    a=l.count(i)
    if a>1:
          for j in range(1,a):
             l.remove(i)
l.sort()
print('LIST AFTER REMOVING DUPLICATES')
print(l)
