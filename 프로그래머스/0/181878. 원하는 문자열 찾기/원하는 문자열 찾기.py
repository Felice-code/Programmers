def solution(myString, pat):
    string, pa = myString.lower(), pat.lower()
    if pa in string:
        return 1
    return 0