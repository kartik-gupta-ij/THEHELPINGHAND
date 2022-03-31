def coin():
    c,b = input().split()
    c=int(c)
    b=int(b)
    if(c==0):
        print(1)
    else:
        print(c+b*2+1)

n= int(input())
for i in range (0,n):
    coin()