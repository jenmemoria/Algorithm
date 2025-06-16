def solution(arr):
    result = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            result.append(i//2)
        elif i < 50 and i % 2 != 0:
            result.append(i*2)
        else: # 아무 조건에 해당하지 않는 것도 생각
            result.append(i)
    return result