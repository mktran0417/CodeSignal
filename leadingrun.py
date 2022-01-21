def solution(a):
    max_count = 0
    count = 1

    if a == []:
        return 0

    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 1

    if max_count < count:
        max_count = count

    return max_count
