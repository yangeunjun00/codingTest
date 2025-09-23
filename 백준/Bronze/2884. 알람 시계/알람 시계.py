h,m = map(int,input().split())
m = m-45
if m<0:
    m = m+60
    h-=1
    if h<0:
        h+=24
print(h ,m)