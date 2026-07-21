def solution(n):
    res = []
    a = ""
    for i in str(n):
        res.append(int(i))
    res.sort()
    res.reverse()
    for i in res:
        a += str(i)
    return int(a)