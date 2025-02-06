def solution(answers):
    correct = [0, 0, 0]
    stud_answer = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i, stud in enumerate(stud_answer):
        numbers =  stud * (len(answers) // len(stud)) + stud[: (len(answers) % len(stud))]
        for j, num in enumerate(numbers):
            if answers[j] == num:
                correct[i] += 1
                
    max_correct = max(correct)
    
    return [i+1 for i,num in enumerate(correct) if num == max_correct ]