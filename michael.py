string = '1234567890'


def solution(s, n):
    if len(s) == 0:
        return 'none'

    if len(s) < n - 1:
        return 'none'

    if n < 0:
        return 'none'

    return s[n]

solution(string, 10)
