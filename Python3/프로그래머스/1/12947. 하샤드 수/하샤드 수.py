def solution(x):
    digitSum = 0
    for digit in str(x):
        digitSum += int(digit)

    return x % digitSum == 0