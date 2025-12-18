import sys
input = sys.stdin.readline
a = int(input())
arr = []
sum = 0
for i in range(a):
    b = int(input())
    if b == 0:
        del arr[-1]
        continue
    arr.append(b)
for j in range(0,len(arr)):
    sum+=arr[j]
print(sum)
