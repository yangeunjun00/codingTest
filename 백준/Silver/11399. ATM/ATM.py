import sys
input = sys.stdin.readline
a = int(input())
sum = 0
num = list(map(int,input().split()))
num.sort()
for i in range(a):
    sum+=num[i]*(a-i)
print(sum)