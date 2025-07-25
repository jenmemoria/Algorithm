def solution(my_string):
    result = ''
    for i in my_string:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            result += i
    return result