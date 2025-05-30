def solution(names):
    '''
    5의 배수
    '''
    result = []
    for idx, i in enumerate(names):
        if idx % 5 == 0:
            result.append(i)
    return result