def solution(n):
    for i in range(1,int(n**0.5)+1):
        if i * i == n:
            return 1
    return 2