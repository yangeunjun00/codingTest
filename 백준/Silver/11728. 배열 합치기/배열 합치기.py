import sys
input = sys.stdin.readline
a,b = map(int,input().split())
arr_1 = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))
for i in range(len(arr_2)):
    arr_1.append(arr_2[i])
arr_1.sort()
for i in arr_1:
    print(i, end=" ")