def solution(a, x):
    count = 0
    b = a.copy()
    for i, val in enumerate(a):
        if val == x:
            b.pop(i - count)
            count += 1
    return b

def solution(a, x):
    return [num for num in a if num != x]