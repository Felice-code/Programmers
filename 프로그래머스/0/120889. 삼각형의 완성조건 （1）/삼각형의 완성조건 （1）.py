def solution(sides):
    sort_sides = sorted(sides)
    if sort_sides[-1] < sort_sides[-2] + sort_sides[-3]:
        return 1
    return 2