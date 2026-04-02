import sys
input = sys.stdin.readline
a = int(input())
num = 0
arr = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))
arr.sort()
arr_2.sort(reverse=True)
for i in range(a):
    num+=arr[i]*arr_2[i]
print(num)
    