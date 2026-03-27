import sys
input=sys.stdin.readline
a = int(input())
list = list(map(int,input().split()))
list_2 = [0]*(a+1)
for i in range(1,a+1):
    list_2[i] = list_2[i-1]+list[i-1]
b = int(input())
for _ in range(b):
    c,d =map(int,input().split())
    print(list_2[d]-list_2[c-1])
    