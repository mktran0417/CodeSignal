def solution(s):
    dicts = {}
    for char in s:
        if dicts.get(char) == None:
            dicts[char] = 1
        else:
            dicts[char] = dicts[char] + 1

    if dicts.get(min(dicts, key=dicts.get)) != 1:
        return '_'
    return min(dicts, key=dicts.get)