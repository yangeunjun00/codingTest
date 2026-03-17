import sys
input = sys.stdin.readline
a = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())
gamdockkwan = 0
for i in range(len(arr)):
    arr[i]-=b
    gamdockkwan+=1
    if arr[i]>0:
        if arr[i]%c!=0:
            gamdockkwan+=(arr[i]//c)+1
        else:
            gamdockkwan+=(arr[i]//c)
    else:
      continue
print(gamdockkwan)