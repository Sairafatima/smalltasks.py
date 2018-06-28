def distance(x1, y1 , x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
x1,y1 = input('Enter the First Point: ').split()
x2,y2 = input('Enter the Second Point: ').split()
x1,x2,y1,y2 = float(x1),float(x2),float(y1),float(y2)
print('The distance between(', x1, y1,') and (', x2, y2, ') is', distance(x1,y1,x2,y2))
