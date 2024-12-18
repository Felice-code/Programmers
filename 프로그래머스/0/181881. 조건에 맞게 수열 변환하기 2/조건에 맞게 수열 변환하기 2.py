def solution(arr):
    x=[]
    for i in range(len(arr)):
        x = arr.copy()
        for j, num in enumerate(arr):
            if num >=50 and num%2==0:
                arr[j] = num//2
            elif num <50 and num%2==1:
                if (num*2)+1 > 100:
                    continue
                arr[j] = (num*2)+1
        if x == arr:
            return i
