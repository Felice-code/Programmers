n, m= map(int, input().split(' '))
card_list = list(map(int, input().split(' ')))

result = 0
lenght = len(card_list)
cnt = 0
for i in range(lenght):
  for j in range(i+1, lenght):
    for k in range(j+1, lenght):
      sum_value = card_list[i] + card_list[j] + card_list[k]
      if sum_value <= m:
        result = max(result, sum_value)
print(result)