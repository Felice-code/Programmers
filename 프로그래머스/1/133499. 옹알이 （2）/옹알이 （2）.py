def solution(babbling):
    possible_sounds = ["aya", "ye", "woo", "ma"]
    count = 0

    for word in babbling:
        for sound in possible_sounds:
            if sound * 2 not in word:
                word = word.replace(sound, " ")
        
        if word.strip() == "":
            count += 1

    return count

