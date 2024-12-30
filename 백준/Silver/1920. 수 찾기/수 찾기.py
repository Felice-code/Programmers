N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_dict = {num:1 for i, num in enumerate(N_list)}
for num in M_list:
  if num in N_dict:
    print(1)
  else:
    print(0)