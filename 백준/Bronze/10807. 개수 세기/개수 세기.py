import sys
input = sys.stdin.readline
a = int(input())
arr = list(map(int,input().split()))
b = int(input())
cnt = 0
for i in range(len(arr)):
    if arr[i] == b:
        cnt+=1
print(cnt)
