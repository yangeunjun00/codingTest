import sys
input = sys.stdin.readline
arr = list(map(int,input().split()))
max = arr[0]
cnt = 0
for i in range(15):
    if arr[i]>max:
        max = arr[i]
        cnt = i
if 14 != cnt:
    print(max+1)
else:
    print(max)