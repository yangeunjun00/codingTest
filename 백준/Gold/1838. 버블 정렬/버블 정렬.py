import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
a = {}

for i in range(n):
    a[numbers[i]] = i
numbers.sort()
b = {}
for j in range(n):
    b[numbers[j]]=j
c = 0
for k in numbers:
   c = max(c,a[k]-b[k])

print(c)
