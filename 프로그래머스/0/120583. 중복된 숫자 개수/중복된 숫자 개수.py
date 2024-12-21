from collections import Counter
def solution(array, n):
    cnt = Counter(array)
    print(cnt)
    return cnt[n]