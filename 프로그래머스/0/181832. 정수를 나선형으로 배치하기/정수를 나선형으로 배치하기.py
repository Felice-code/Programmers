def solution(n):
    arr = [[0]*n for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    
    x, y = 0, 0
    for i in range(1, n*n + 1):
        arr[x][y] = i
        
        next_x = x + directions[direction_index][0]
        next_y = y + directions[direction_index][1]
        
        if not (0 <= next_x < n and 0 <= next_y < n and arr[next_x][next_y] == 0):
            direction_index = (direction_index + 1) % 4
            next_x = x + directions[direction_index][0]
            next_y = y + directions[direction_index][1]
        
        x, y = next_x, next_y
    
    return arr
