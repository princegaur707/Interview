def sum(a,b):
    if b==0:
        return a
    else:
        return sum(a^b,(a&b)<<1)
while True:
    a,b=map(int,input().split())
    print(sum(a,b))