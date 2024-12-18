def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        cnt = 0
        num = num_list[i]
        # num이 1이 될 때까지 반복
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num - 1) // 2
            cnt += 1
        answer += cnt
    return answer
