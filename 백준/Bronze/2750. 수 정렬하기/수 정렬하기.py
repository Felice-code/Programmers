N = int(input().strip())
aa = []
for _ in range(N):
    aa.append(int(input().strip()))

aa.sort()
print('\n'.join(map(str, aa)))