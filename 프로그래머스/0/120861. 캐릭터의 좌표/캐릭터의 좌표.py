def solution(keyinput, board):
    key_map = {
        'left':(-1,0),
        'right':(1,0),
        'up':(0,1),
        'down':(0,-1)
    }
    size_x, size_y = board[0]//2, board[1]//2
    x, y = 0,0
    for key in keyinput:
        move_x, move_y = key_map[key]
        if abs(move_x+x) <= size_x and abs(move_y+y) <=size_y:
            x += move_x
            y += move_y
    return [x,y]
            
        
        