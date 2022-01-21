def solution(current):
    num = int(current)

    while True:
        num += 1
        if len(str(num)) != 7:
            current =  '0' * (6 - len(str(num))) + str(num)
            if current == current[::-1]:
                return current
        else:
            break
    return '000000'
