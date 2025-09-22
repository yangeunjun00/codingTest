a = int(input())
s = 0 
b = int(input())
while b>0:
        s += b%10
        b = b//10
print(s)