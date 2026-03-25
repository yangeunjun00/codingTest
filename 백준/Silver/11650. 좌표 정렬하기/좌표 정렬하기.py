import sys
input = sys.stdin.readline
a = int(input())
pig = []
for _ in range(a):
    k,v = map(int,input().split())
    pig.append((k,v))
for key,value in sorted(pig):
    print(key,value)
