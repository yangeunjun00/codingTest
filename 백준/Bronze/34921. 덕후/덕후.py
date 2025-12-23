import sys
input = sys.stdin.readline
a,b = map(int,input().split())
if 10+2*(25-a+b)<=0:
    print(0)
else:
    print(10+2*(25-a+b))