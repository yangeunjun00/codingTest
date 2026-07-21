def solution(s):
    p_cnt = 0
    y_cnt = 0
    s = s.lower()
    for i in s:
        if i == "p":
            p_cnt+=1
        elif i == "y":
            y_cnt+=1
    if p_cnt == y_cnt:
        return True
    elif p_cnt == 0 and y_cnt ==0:
        return True
    else:
        return False
    
