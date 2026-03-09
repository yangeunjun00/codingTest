import sys
input = sys.stdin.readline
sum = 0
a = int(input())
for j in range(a):
    input()
    b = int(input())
    for i in range(b):
        temp = int(input())
        sum+=temp
    if sum%b==0:
        print("YES")
    else:
        print("NO")
    sum = 0
