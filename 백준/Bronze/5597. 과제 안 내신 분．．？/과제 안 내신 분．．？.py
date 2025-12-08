import sys
input = sys.stdin.readline
arr = [1]*31
num = [0]*31
cnt = 0
for i in range(28):
    a = int(input())
    num[a] = 1
for j in range(1,31):
    if arr[j]!=num[j]:
        cnt = j
        print(cnt)