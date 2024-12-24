n_list= list(map(int, input().split(' ')))
original = n_list.copy()
if sorted(original) ==n_list:
  print('ascending')
elif sorted(original, reverse = True) == n_list:
  print('descending')
else:
  print('mixed')