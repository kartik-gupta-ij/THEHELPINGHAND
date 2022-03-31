def cp():
    n=int(input())
    c = [int(num) for num in input().split(" ", n-1)]
    m=max(c)
    m=m-1
    if(c.count(m)>1):
        print("YES")
    else:
        print("NO")

n=int(input())
for i in range (0,n):
    cp()
