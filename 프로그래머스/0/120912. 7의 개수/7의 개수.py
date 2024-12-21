def solution(array):
    answer = ''.join(str(arr) for arr in array)
    cnt = 0
    for i in answer:
        if int(i) == 7:
            cnt+=1
    return cnt