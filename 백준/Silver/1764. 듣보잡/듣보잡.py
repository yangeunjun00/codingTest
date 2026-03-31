import sys
input = sys.stdin.readline
a,b = map(int,input().split())
arr = []
arr_2 = []
for i in range(a):
    pig = input()
    arr.append(pig)
for j in range(b):
    pig = input()
    arr_2.append(pig)
arr = set(arr)
arr_2 = set(arr_2)
arr_3 = list(arr&arr_2)
arr_3.sort()
print(len(arr_3))
for k in arr_3:
    print(end=k)
