def solution(a):
    count = 0

    if len(a) == 1:
        if a[0] == 0:
            return 1
        else:
            return count

    if a[1] / 2 == a[0]:
        count += 1

    for i in range(1, len(a) - 1):
        if (a[i - 1] + a[i + 1]) / 2 == a[i]:
            count +=1

    if a[len(a) - 2] / 2 == a[len(a) - 1]:
        count += 1
    return count