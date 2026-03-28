import sys
input = sys.stdin.readline
a,b = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
for i in range(a-1,-1,-1):
    temp = 0
    for j in range(1,i+1):
        if arr[temp]<arr[j]:
            temp = j
    if temp==i:
        continue
    cnt+=1
    arr[i],arr[temp]=arr[temp],arr[i]
    if cnt==b:
        print(*arr)
if cnt<b:
    print(-1)


