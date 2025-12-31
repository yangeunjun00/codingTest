import sys
input = sys.stdin.readline
a = int(input())
b=0
if a%5==0:
    print(a//5)
else:
    while a>0:
        a-=3
        b+=1
        if a%5==0:
            b+=a//5
            print(b)
            break
        elif a==0:
            print(b)
            break
        elif a==1 or a==2:
            print(-1)
            break
