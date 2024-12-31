N = input()

N_list = [int(num) for num in N]
N_list.sort(reverse = True)
print(''.join(map(str,N_list)))
