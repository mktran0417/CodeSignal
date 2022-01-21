def solution(a):
    count = 0

    if len(a) < 3:
        return count

    for i in range(1, len(a) - 1):
        if is_good(a[i - 1], a[i], a[i + 1]):
            count += 1
    return count


def is_good(a, b, c):
    if a == c and a == b:
        return False
    if a == b or a == c or b == c:
        return True
    return False




solution([1, 1, 1, 2, 1, 3, 4])
