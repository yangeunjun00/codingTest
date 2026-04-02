import sys
input = sys.stdin.readline
int(input())
arr = list(map(int,input().split()))
arr.sort()
print(*arr)