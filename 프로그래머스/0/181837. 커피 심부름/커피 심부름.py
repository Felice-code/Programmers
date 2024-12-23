def solution(orders):
    answer = 0
    for order in orders:
        if 'cafelatte' in order:
            answer += 5000
        elif 'americano' in order:
            answer += 4500
        else:
            answer += 4500
    return answer