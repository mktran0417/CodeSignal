def solution(digits):
    carry = 0
    n = len(digits) - 1

    for i, value in enumerate(reversed(digits)):
        if value >= 9:
            digits[n - i] = 0
            carry = 1
        else:
            digits[n - i] = digits[n - i] + 1
            return digits

    if carry == 1:
        digits.insert(0, 1)

    return digits
