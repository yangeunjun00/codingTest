import sys
input = sys.stdin.readline
a = int(input())
a_copy = a
b = int(input())
num = 0
final = 0
for i in range(3):
    for j in range(3):
        num += (a%10*(b%10))*10**j
        a = a//10 
    print(num)
    final+=num*10**i
    a = a_copy
    b = b//10
    num = 0
print(final)