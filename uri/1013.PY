

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
x = (a+b+abs(a-b))/2
y = (x+c+abs(x-c))/2
y = int(y)
print("%i eh o maior" %(y))