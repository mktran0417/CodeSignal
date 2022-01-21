def solution(inputString):
    temp = inputString[0]
    count = 1
    output = ''
    for char in inputString[1::]:
        if temp == char:
            count +=1
        else:
            output += str(count) + temp
            temp = char
            count = 1
    output += str(count) + temp
    return output


