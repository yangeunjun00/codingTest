import sys
input = sys.stdin.readline
a = int(input())
arr = [int(b) for b in str(a)]
for i in range(0,len(arr),1):
    for j in range(0,len(arr)-1,1):
        if arr[j]<arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1]=temp
c = int(''.join(map(str,arr)))
print(c)