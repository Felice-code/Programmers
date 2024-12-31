import sys
N = int(sys.stdin.readline())
aa = [0] * 10001
for i in range(N):
    data = int(sys.stdin.readline())
    aa[data] += 1

for i in range(10001):
  if aa[i] != 0:
    for j in range(aa[i]):
      print(i)