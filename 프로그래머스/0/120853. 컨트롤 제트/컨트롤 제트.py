def solution(s):
    answer = 0
    print(list(s.split(' ')))
    arr = list(s.split(' '))
    for i in range(len(arr)):
        if arr[i] == 'Z':
            answer = answer - int(arr[i-1])
        else:
            answer += int(arr[i])
    return answer