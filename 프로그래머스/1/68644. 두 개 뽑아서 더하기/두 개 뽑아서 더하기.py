def solution(numbers):
    answer = []
    for i,num in enumerate(numbers):
        for j in range(i+1,len(numbers)):
            answer.append(num+numbers[j])
    temp = set(answer)
    r = list(temp)
    a = sorted(r)
    return a