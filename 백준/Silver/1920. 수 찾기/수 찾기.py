import sys
input = sys.stdin.readline
a = int(input())
arr = set(map(int,input().split()))
b = int(input())
arr_2 = list(map(int,input().split()))
for saehaebokmani in arr_2:
    if saehaebokmani in arr:
        print(1)
    else:
        print(0)
