def solution(n):
    number = 0
    while n > 0 :
        mod = n % 10
        number =  number * 10 + mod
        n //= 10

    return number