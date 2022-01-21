def solution(a, window_size):
    results = []
    for i in range(0, len(a) - window_size + 1, 1):
        average = 0
        for j in range(window_size):
            average += a[i + j]
        average /= window_size
        results.append(average)
    return results