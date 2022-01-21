def solution(s, x):
    for i in range(0, len(s) - len(x) + 1, 1):
        if s[i: i + len(x)] == x:
            return i
    return -1


def solution(s, x):
    for i in range(0, len(s) - len(x) + 1, 1):
        for j in range(len(x)):
            if s[i + j] != x[j]:
                break
            if j == len(x) - 1 and s[i + j] == x[j]:
                return i
    return -1
