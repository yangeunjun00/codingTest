import sys
input = sys.stdin.readline
a = int(input())
arr = set()
for _ in range(a):
    b,c = map(str,input().split())
    if c == "enter":
        arr.add(b)
    elif c=="leave":
        arr.discard(b)
arr = sorted(arr,reverse=True)
print(*arr, sep='\n')