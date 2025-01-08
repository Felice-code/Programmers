def solution(a, b, n):
    answer = 0
    while True:
        answer += (n//a)*b
        n = (n-(n-(n%a))+((n//a)*b))
        print(n,answer)
        if (n//a) == 0:
            break
    
    return answer