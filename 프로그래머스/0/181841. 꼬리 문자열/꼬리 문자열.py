def solution(str_list, ex):
    return ''.join(string for string in str_list if ex not in string)