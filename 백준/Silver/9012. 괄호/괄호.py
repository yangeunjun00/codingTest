import sys
input = sys.stdin.readline
stack = []
a = int(input())
cnt=0
for i in range(a):
    str = input()
    str = list(str)
    for j in range(len(str)):
        if str[j]==')':
          if len(stack)==0:
            stack.append(j)
            break
          stack.pop()
          
        if str[j]=='(':
            stack.append(j)
    if len(stack)==0:
        print("YES")
    else:
        print("NO")
    stack = []
