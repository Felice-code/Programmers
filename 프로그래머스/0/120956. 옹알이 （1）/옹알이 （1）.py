def solution(babbling):
    valid_words = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        for valid in valid_words:
            if valid * 2 in word: 
                break
            word = word.replace(valid, " ")
        if word.strip() == "":  
            count += 1

    return count
