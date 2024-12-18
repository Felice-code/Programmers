def solution(my_string):
    arr_dic = {key:cnt for cnt, key in enumerate(my_string)}
    return ''.join(arr_dic.keys())