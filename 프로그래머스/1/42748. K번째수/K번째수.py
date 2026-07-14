def solution(array, commands):
    answer = []
    hi = array[:]
    for i in range(len(commands)):
        array= array[commands[i][0]-1:commands[i][1]]
        array.sort()
        answer.append(array[commands[i][2]-1])
        array = hi
    return answer