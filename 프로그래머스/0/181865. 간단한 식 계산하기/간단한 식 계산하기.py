def calculator(a, b, symbol):
    if symbol == "+":
        return a + b
    elif symbol =='-':
        return a - b
    else:
        return a * b
def solution(binomial):
    arr = binomial.split(' ')
    return calculator(int(arr[0]), int(arr[2]), arr[1])