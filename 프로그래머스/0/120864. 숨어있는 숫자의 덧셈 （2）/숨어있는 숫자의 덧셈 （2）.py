def solution(my_string):
    sum_value = 0
    num = ''
    
    for char in my_string:
        if char.isdigit():
            num += char
        else:
            if num:
                sum_value += int(num)
                num = ''
    
    if num:
        sum_value += int(num)
    
    return sum_value

