def solution(spell, dic):
    for word in dic:
        if all(char in word for char in spell):
            return 1
    return 2
