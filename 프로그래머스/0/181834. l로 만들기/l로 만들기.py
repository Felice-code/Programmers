def solution(myString):
    answer = ''
    
    return ''.join('l' if ord(string) < ord('l') else string  for string in myString)