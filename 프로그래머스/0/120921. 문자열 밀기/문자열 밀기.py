from collections import deque

def solution(A, B):
    if A == B:
        return 0
    de = deque(A)
    ans_de = deque(B)
    for i in range(len(A)):
        de.rotate(1)
        if de == ans_de:
            return i+1
    return -1