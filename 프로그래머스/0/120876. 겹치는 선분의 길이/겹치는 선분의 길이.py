def solution(lines):
    coords = [0] * 201
    for start, end in lines:
        for i in range(start, end):
            coords[i + 100] += 1

    overlap_length = sum(1 for x in coords if x > 1)
    return overlap_length
