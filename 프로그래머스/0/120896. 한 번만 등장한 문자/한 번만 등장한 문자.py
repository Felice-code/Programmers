def solution(s):
    # 각 문자의 빈도 계산
    from collections import Counter
    counts = Counter(s)

    # 최소 빈도를 가진 문자들만 정렬 후 반환
    min_count = min(counts.values())
    result = sorted([char for char, count in counts.items() if count == min_count])
    
    return ''.join(result)
