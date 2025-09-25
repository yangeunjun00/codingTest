a = int(input())
b = int(input())
c = int(input())
r = list(str(a*b*c))
for i in range(0,10):
    s = 0
    for j in range(len(r)):
        if(int(r[j])==i):
           s+=1
    print(s)