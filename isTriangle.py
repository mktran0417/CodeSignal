def solution(arr):
    triangle = []
    for i in range(len(arr) - 2):
        triangle.append(is_triangle(arr[i], arr[i + 1], arr[i + 2]))
    return triangle


def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return 1
    return 0
