def solution(myString, pat):
    answer = []
    for i, string in enumerate(myString):
        if string == pat[0] and myString[i:i+len(pat)] == pat:
            answer.append(myString[:i+len(pat)])
    return max(answer)