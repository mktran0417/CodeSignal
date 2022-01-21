def solution(string, words):
    dict = {}
    for word in string.split(' '):
        if dict.get(word) == None and word not in words:
            dict.update({word: 1})
    return len(dict)

string = 'hakuna matata what a wonderful phrase a'
words = ['hakuna', 'matata']

print(solution(string, words))


