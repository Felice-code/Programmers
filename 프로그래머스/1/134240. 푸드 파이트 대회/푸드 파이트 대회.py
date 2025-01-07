def solution(food):
    answer = ''
    for i, num in enumerate(food[1:]):
        answer += (str(i+1) * (num//2))
    answer += '0'
    for string in answer[-2::-1]:
        answer += str(string)
    return answer