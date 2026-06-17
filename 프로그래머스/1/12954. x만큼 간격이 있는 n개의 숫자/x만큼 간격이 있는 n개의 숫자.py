def solution(x, n):
    answer = [0]*(n+1)
    for i in range(1,len(answer)):
        
        answer[i] = x*i
    return answer[1:n+1]