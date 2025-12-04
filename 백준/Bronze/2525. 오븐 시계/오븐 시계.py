import sys
input = sys.stdin.readline
h,m = map(int,input().split())
c = int(input())
m = m+c
if m>59:
        h += m//60
        m = m%60
if h>23:
    h-=24
print(h,m)
