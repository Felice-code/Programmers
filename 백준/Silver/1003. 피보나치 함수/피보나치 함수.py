import sys

def solve():
    T = int(sys.stdin.readline().strip())  # 테스트 케이스 개수
    
    # 0과 1이 각각 몇 번 출력되는지 저장할 리스트 (N은 최대 40)
    count0 = [0] * 41
    count1 = [0] * 41

    # 초기값 설정 (fibonacci(0) = 0 한 번 출력, fibonacci(1) = 1 한 번 출력)
    count0[0] = 1
    count1[0] = 0
    count0[1] = 0
    count1[1] = 1

    # DP 테이블 채우기
    for i in range(2, 41):
        count0[i] = count0[i - 1] + count0[i - 2]
        count1[i] = count1[i - 1] + count1[i - 2]

    # 각 테스트 케이스에 대해 결과 출력
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        print(count0[N], count1[N])

# 메인 루틴
if __name__ == "__main__":
    solve()
