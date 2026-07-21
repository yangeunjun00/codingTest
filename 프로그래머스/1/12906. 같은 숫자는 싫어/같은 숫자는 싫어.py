def solution(arr):
    res = []
    for i in arr:
        if res and res[-1] == i:
            continue
        res.append(i)
    return res