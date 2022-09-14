def sum(x,y):
    d = x +y
    
    if d >= 15 and d <= 20:
        return 20
    else:
        return d
a , b = map(int, input().split())
print(sum(a,b))