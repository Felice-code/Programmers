def solution(price, money, count):
    sum_price = sum(price* i for i in range(1,count+1))
    if sum_price > money:
        return sum_price - money
    return 0