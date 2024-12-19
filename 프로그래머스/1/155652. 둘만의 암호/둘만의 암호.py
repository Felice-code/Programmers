def solution(s, skip, index):
    answer = ''
    skip_set = set(ord(char) for char in skip)  # skip_ord를 set으로 변환
    for char in s:
        num = ord(char)
        cnt = 0
        while cnt < index:
            num += 1
            if num > 122:  # z를 넘어가면 a로 순환
                num = 97
            if num not in skip_set:  # skip 문자에 포함되지 않을 때만 증가
                cnt += 1
        answer += chr(num)
    return answer
