def solution(array):
    switch = True;
    # even == True
    # odd == false
    if array[0] % 2 == 0:
        switch = False
    else:
        switch = True

    for i, value in enumerate(array):
        # if value is even and the previous number was even
        if value % 2 == 0 and switch:
            return i
        # if value is odd and the previous number was odd
        if value % 2 == 1 and not switch:
            return i
        # flip switch if neither of the above was true
        switch = not switch
    return -1


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 3, 4, 5]))
print(solution([2, 4, 3, 4, 5]))
print(solution([2, 5, 4, 4, 5]))


def solution_a(n):
    for i in range(len(n) - 1):
        if n[i] % 2 == 1 and n[i + 1] % 2 == 1:
            return i + 1
        elif n[i] % 2 == 0 and n[i + 1] % 2 == 0:
            return i + 1
    return -1


print(solution_a([1, 2, 3, 4, 5]))
print(solution_a([1, 3, 3, 4, 5]))
print(solution_a([2, 4, 3, 4, 5]))
print(solution_a([2, 5, 4, 4, 5]))
