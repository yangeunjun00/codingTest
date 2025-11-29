import sys
a = int(sys.stdin.readline().strip())
lines = []
for i in range(a):
    line = int(sys.stdin.readline().strip())
    lines.append(line)
    
lines.sort()
for i in range(len(lines)):
    print(lines[i])




