def solution(d, budget):
    d.sort()  # 신청한 금액을 오름차순으로 정렬합니다.
    total = 0  # 현재까지 지원한 금액의 총합
    count = 0  # 지원할 수 있는 부서의 수

    for amount in d:
        if total + amount <= budget:  # 현재까지의 총합에 신청한 금액을 더해도 예산을 초과하지 않는 경우
            total += amount  # 총합에 해당 부서의 신청 금액을 더합니다.
            count += 1  # 지원할 수 있는 부서의 수를 1 증가시킵니다.
        else:
            break  # 예산을 초과하는 경우 반복을 종료합니다.

    return count  # 지원할 수 있는 부서의 수를 반환합니다.
