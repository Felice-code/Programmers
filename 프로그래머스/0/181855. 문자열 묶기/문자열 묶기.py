from collections import Counter
def solution(strArr):
    new_str = [len(string) for string in strArr]
    counter = Counter(new_str).most_common(1)
    return counter[0][1]