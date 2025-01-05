from collections import deque

def solve():
    N, M = map(int, input().split())
    positions = list(map(int, input().split()))

    dq = deque(range(1, N + 1))
    total_operations = 0

    for pos in positions:
        idx = dq.index(pos)
       
        left_moves = idx
        right_moves = len(dq) - idx

        
        if left_moves <= right_moves:
            dq.rotate(-left_moves)  
            total_operations += left_moves
        else:
            dq.rotate(right_moves)  
            total_operations += right_moves

        dq.popleft()

    print(total_operations)


solve()
