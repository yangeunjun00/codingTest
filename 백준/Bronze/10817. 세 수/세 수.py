import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())
arr =[]
arr.append(a)
arr.append(b)
arr.append(c)
arr.remove(max(arr))
print(max(arr))