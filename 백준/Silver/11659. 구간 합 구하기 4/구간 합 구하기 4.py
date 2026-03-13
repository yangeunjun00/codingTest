import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = list(map(int,input().split()))
ssyagal = [0]*(N+1)
for i in range(1,N+1):
    ssyagal[i] = ssyagal[i-1] + arr[i-1]
for j in range(M):
    a,b = map(int,input().split())
    print(ssyagal[b]-ssyagal[a-1])

