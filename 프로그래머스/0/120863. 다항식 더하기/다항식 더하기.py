def solution(polynomial):
    terms = polynomial.split(' + ')
    x_sum = 0
    const_sum = 0
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term.replace('x', ''))
        else:
            const_sum += int(term)
    
    if x_sum == 0:
        return str(const_sum)
    elif x_sum == 1:
        if const_sum == 0:
            return 'x'
        else:
            return f'x + {const_sum}'
    else:
        if const_sum == 0:
            return f'{x_sum}x'
        else:
            return f'{x_sum}x + {const_sum}'


        