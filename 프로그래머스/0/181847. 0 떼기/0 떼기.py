def solution(n_str):
    
    for i, num in enumerate(n_str):
        if n_str[0] == '0':
            n_str = n_str[1:]
    
    return n_str