def fib(n):
    if n<=1:
        return 1
    return n*fib(n-1)
import sys
input = sys.stdin.readline
print(fib(int(input())))