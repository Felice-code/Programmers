def solution(X, Y):
    freq_x = [0] * 10
    freq_y = [0] * 10

    for char in X:
        freq_x[int(char)] += 1
    for char in Y:
        freq_y[int(char)] += 1
        
    answer = []
    for digit in range(10):
        common_count = min(freq_x[digit], freq_y[digit])
        answer.extend([str(digit)] * common_count)

    if not answer:
        return "-1"

    if all(num == "0" for num in answer):
        return "0"

    return ''.join(sorted(answer, reverse=True))