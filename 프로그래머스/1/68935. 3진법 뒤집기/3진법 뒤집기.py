def solution(n):
    answer = ''
    value = 0
    while n >=3:
        answer += str(n%3)
        n = n//3
    answer += str(n)
    for i in range(len(answer)):
        value += 3**i * int(answer[-(i+1)])
        
    return value

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer