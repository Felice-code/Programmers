def solution(k, score):
    hall_of_fame = []  
    result = []  

    for s in score:
        hall_of_fame.append(s)  
        hall_of_fame.sort(reverse=True) 

        if len(hall_of_fame) > k:
            hall_of_fame.pop()  

        result.append(hall_of_fame[-1])
    
    return result
