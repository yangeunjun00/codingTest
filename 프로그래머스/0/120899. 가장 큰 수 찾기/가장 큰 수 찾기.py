def solution(array):
    answer = []
    hi = max(array)
    answer.append(hi)
    for i in range(len(array)):
        if hi == array[i]:
            answer.append(i)
    
    return answer