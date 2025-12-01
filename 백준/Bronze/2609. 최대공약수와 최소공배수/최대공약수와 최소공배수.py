import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
s = 0
d = 0

z = b if a>b else a
for i in range(1,z+1):
    if a % i== 0 and b % i == 0:
        s = i
print(s,a*b//s,sep="\n")