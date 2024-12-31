N = int(input())
age_list = []
for _ in range(N):
    age, name = input().split()
    age_list.append([int(age), name])

age_list.sort(key=lambda x: x[0])  # 나이(age)가 들어 있는 x[0]을 기준으로 정렬

for age, name in age_list:
    print(age, name)