import sys
input = sys.stdin.readline
a = int(input())
b = set(map(int,input().split()))
b = list(b)
for i in range(len(b)):
    for j in range(0,len(b)-i-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
for i in range(len(b)):
    print(str(b[i]),end=" ")