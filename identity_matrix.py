def solution(size):
    arr = []
    for i in range(size):
        row = []
        for j in range(size):
            if i != j:
                row.append(0)
            else:
                row.append(1)
        arr.append(row)
    return arr
