def solution(arr):
    answer = [[]]
    x, y = len(arr[0]), len(arr)
    print(x,y)
    if x == y:
        return arr
    if x<y:
        for i in range(y):
            for j in range(y-x):
                arr[i] += [0]
        return arr
    elif x > y:
        for i in range(y):
            if len(arr[i]) == x:
                continue
            elif len(arr[i]) != x:
                arr[i] += ([0]*(x-y))
        arr += [[0]*x for a in range(x-y)]
        return arr
        