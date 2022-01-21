def solution(a):
    count = 1
    if len(a) == 0:
        return 0

    for i in a[1::]:
        if a[0] == i:
            count += 1
        else:
            break
    return count