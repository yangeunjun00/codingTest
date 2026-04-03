import sys
input = sys.stdin.readline
a ,b= map(int,(input().split()))
pig = set(map(int,input().split()))
pig2 = set(map(int,input().split()))
b = len(pig-pig2)+len(pig2-pig)
print(b)
