def solution(numbers):

    numbers.sort()
    

    max_product = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    
    return max_product
