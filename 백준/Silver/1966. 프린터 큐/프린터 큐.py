from collections import deque


T = int(input().strip())  # 테스트 케이스 수
    
for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
        
    queue = deque((p, i) for i, p in enumerate(priorities))
        
    print_order = 0  
        
    while queue:
        current = queue[0] 

        if any(current[0] < q[0] for q in queue):
            queue.rotate(-1)
        else:
            # 인쇄(큐에서 제거)
            print_order += 1
            printed_doc = queue.popleft()

            if printed_doc[1] == M:
                print(print_order)
                break