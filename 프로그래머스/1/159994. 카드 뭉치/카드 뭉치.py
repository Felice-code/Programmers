def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0
    for string in goal:
        if cards1[idx1] == string:
            if idx1 < len(cards1)-1:
                idx1+=1
            
        elif cards2[idx2] == string:
            if idx2 < len(cards2)-1:
                idx2+=1
        else:
            return "No"
        
    return 'Yes'