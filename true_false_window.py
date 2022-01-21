def solution(a, window_size):
    results = []
    for i in range(0, len(a) - window_size + 1, 1):
        switch = True
        for j in range(window_size):
            if a[i + j] % 2 == 0:
                switch = False
                break;
        results.append(switch)
    return results
