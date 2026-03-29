def fac(n):
    if n==0 or n==1:
        return 1
    return n*fac(n-1)
import sys
input = sys.stdin.readline
a,b = map(int,input().split())
print(fac(a)//(fac(b)*fac(a-b)))
