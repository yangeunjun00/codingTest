import sys
input = sys.stdin.readline
a = int(input())
arr = []
for _ in range(a):
    b = int(input())
    arr.append(b)
arr.sort(reverse=True)
print(*arr,sep='\n')