def solution(myString, pat):
    string, pa = myString.lower(), pat.lower()
    if len(myString) < len(pat):
        return 0
    if pa in string:
        return 1
    return 0