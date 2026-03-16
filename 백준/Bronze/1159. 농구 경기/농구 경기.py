import sys
input = sys.stdin.readline
a = int(input())
arr = []
ztz = {}
cnt = 0
for i in range(a):
    b = input().strip()
    if b[0] not in ztz:
        ztz[b[0]] =1
    else:
        ztz[b[0]] +=1
for key,value in sorted(ztz.items()):
    if value >= 5:
        print(end=key)
    elif value < 5:
        cnt+=1
if cnt == len(ztz):
    print("PREDAJA")

    
    