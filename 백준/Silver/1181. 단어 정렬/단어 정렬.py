import sys
input = sys.stdin.readline
a = int(input())
arr = []
for i in range(a):
    str = input()
    arr.append(str)
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
for m in range(len(arr)):
    print(end=arr[m])