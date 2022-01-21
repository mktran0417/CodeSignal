from cgitb import small
from timeit import default_timer as timer
from datetime import timedelta
import sys
import math


def find_combinations(A, k, subarrays, out=(), i=0):
    if len(A) == 0 or k > len(A):
        return

    if k == 0:
        subarrays.add(out)
        return

    for j in range(i, len(A)):
        find_combinations(A, k - 1, subarrays, out + (A[j],), j + 1)

def solution_two(p):
    p.sort()
    p = tuple(map(tuple, p))

    subarrays = set()
    points_perm = {}
    for i in range(len(p)):
        for j in range(len(p)):
            if i != j and points_perm.get((p[i], p[j])) == None:
                points_perm[(p[i], p[j])] = \
                    ((p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2) ** (1/2)

    return points_perm.get(min(points_perm, key=points_perm.get))


test = [[0, 11],
        [-7, 1],
        [-5, -3]]


def solution_three(p):
    p.sort()

    smallest = sys.maxsize
    for i in range(len(p)):
        print(p[i])
        euclidean = \
            (p[i][0] - p[i][0]) ** 2 + (p[i][1] - p[i][1]) ** 2
        if smallest > euclidean:
            smallest = euclidean
    return math.sqrt(smallest)


def compare_x(a, b):
    if a > b:
        return a
    return b


def compare_y(a, b):
    if a > b:
        return a
    return b

def dist(p1, p2):
    return math.sqrt((p1[0][0] - p2[0][0]) ** 2 + (p1[0][1] - p2[0][1]) ** 2)

def bruteForce(p, n):
    smallest = sys.maxsize

    for i in range(len(p)):
        for j in range(i, len(p)):
            if dist(p[i], p[j]) < smallest:
                smallest=dist(p[i], p[j])
    return smallest

def solution(p, n):
    px = p.copy()
    py = p.copy()
    px.sort(key=compare_x)
    px.sort(key=compare_x)
    return closest_util(px, py, n)

def closest_util(px, py, n):
    if n <= 3:
        return bruteForce(px, n)

    mid = n // 2
    midpoint = px[mid]
    pyl = py[0:mid]
    pyr = py[mid:len(py)]

    dl = closest_util(px, pyl, mid)
    dr = closest_util(px[mid] , pyl, n - mid)

    d = min(dl, dr)

    strip = []
    count = 0
    for i in range(n):
        if abs(py[i][0] - midpoint[0] < d):
            strip.append(py[i])

    return strip_closet(strip, j, d)

