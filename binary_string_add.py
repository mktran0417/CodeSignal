def solution(a, b):
    carry = 0
    binary = ''

    if(len(a) > len(b)):
        b = ('0') * (len(a) - len(b)) + b
    else:
        a = ('0') * (len(b) - len(a)) + a

    n = len(a) - 1

    for i in range(len(a)):
        carry += int(a[n - i]) + int(b[n - i])
        if carry == 2:
            carry = 1
            binary = '0' + binary
        elif carry > 2:
            carry = 1
            binary = '1' + binary
        elif carry == 1:
            carry = 0
            binary = '1' + binary
        elif carry == 0:
            binary = '0' + binary

    if carry == 1:
        binary = '1' + binary

    return binary
