def solution(s):
    answer = ''
    answer_dic = {char:0 for char in set(s)}
    for char in s:
        answer_dic[char] += 1
    for char, val in answer_dic.items():
        if val == min(answer_dic.values()):
            answer+=char

    return ''.join(sorted(answer))