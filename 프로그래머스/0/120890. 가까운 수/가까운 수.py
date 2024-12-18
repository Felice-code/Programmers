def solution(array, n):
    # 배열을 차이값 기준으로 정렬, 차이가 같은 경우 숫자 자체로 정렬
    array.sort(key=lambda x: (abs(x - n), x))
    return array[0]
