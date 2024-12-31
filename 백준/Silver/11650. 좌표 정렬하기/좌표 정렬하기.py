N = int(input())
aa = []
for _ in range(N):
    a, b = map(int, input().split(' '))
    aa.append([a,b])
aa.sort(key=lambda p: (p[0], p[1]))

for x, y in aa:
    print(x, y)
