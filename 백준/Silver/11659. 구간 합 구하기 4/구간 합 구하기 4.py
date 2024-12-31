import sys

input = sys.stdin.readline

N, M = map(int, input().split()) 
nums = list(map(int, input().split())) 

p = [0] * (N + 1)
for i in range(1, N + 1):
    p[i] = p[i-1] + nums[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(p[j] - p[i-1])
