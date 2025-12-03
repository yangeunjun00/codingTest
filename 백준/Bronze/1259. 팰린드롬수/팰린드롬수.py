import sys
input = sys.stdin.readline

while (a:=int(input())):
    b = [int(d) for d in str(a)]
    pal = True
    for i in range(0,int(len(b))//2):
        if b[i] != b[-1-i]:
            pal = False 
            break
    if pal == True:
        print("yes")
    else :
        print("no")
