import sys
input = sys.stdin.readline
arr = [1,1,2,2,2,8]
arr_2 = list(map(int,input().split()))
for i in range(6):
    if arr[i] != arr_2[i]:
        print(arr[i]-arr_2[i],"",end="")
    else:
        print("0 ",end="")