def solution(picture, k):
    enlarged_picture = []
    
    for row in picture:
        enlarged_row = ''.join(char * k for char in row)
        for _ in range(k):
            enlarged_picture.append(enlarged_row)
    return enlarged_picture

