def solution(myString):
    answer =''
    string = myString.lower()
    for i, strin in enumerate(string):
        if strin == 'a':
            answer += strin.upper()
        else:
            answer += strin
    return answer