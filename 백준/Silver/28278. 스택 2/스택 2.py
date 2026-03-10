import sys
input = sys.stdin.readline
a = int(input())
stack = []
for i in range(a): 
    b = list(map(int,input().split()))
    if b[0]==1:
        stack.append(b[1])
    if b[0]==2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if b[0]==3:
        print(len(stack))
    if b[0]==4:
        if stack:
            print(0)
        else:
            print(1)
    if b[0]==5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    


