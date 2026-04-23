import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    b,c,d,e,f = map(str,input().split())
    b=int(b)
    d=int(d)
    f=int(f)
    if c == "+":
        if b+d==f:
            print("correct")
        else:
            print("wrong answer")
    if c == "-":
        if b-d==f:
            print("correct")
        else:
            print("wrong answer")
    if c == "*":
        if b*d==f:
            print("correct")
        else:
            print("wrong answer")
    if c == "/":
        if b/d==f:
            print("correct")
        else:
            print("wrong answer")