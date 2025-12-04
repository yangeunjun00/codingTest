import sys
input = sys.stdin.readline
a = list(map(int,input().split()))
cnt = 0
max = a[0]
same = 0

for j in range(3):
    if a[j] > max:
        max = a[j]

if a[0]==a[1] and a[0]==a[2]:
    cnt = 2
    same = a[0]

elif a[0] == a[1]:
    cnt =1
    same = a[0]

elif a[0] == a[2]:
    cnt=1
    same = a[2]

elif a[1] == a[2]:
    cnt=1
    same = a[2]

if cnt == 0:
    print(max*100)
elif cnt == 1:
    print(1000+same*100)
elif cnt == 2:
    print(10000+same*1000)
