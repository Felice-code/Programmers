def solution(number, limit, power):
    # 약수 개수 계산 함수
    def count_divisors(n):
        count = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                count += 1
                if i != n // i:  # 제곱수가 아닐 경우
                    count += 1
        return count

    total_weight = 0
    for i in range(1, number + 1):
        divisors_count = count_divisors(i)
        # 공격력 계산
        if divisors_count > limit:
            total_weight += power
        else:
            total_weight += divisors_count

    return total_weight
