def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        min_value = min(arr)
        return [x for x in arr if x != min_value]
