def solution(array, n):
    answer = 0
    array.sort()				#중복 값일 때 최소를 위해서
    a = []
    for i in array:
        a.append(abs(i-n))      #17, 10, 8
    b = a.index(min(a))         # b = 2
    answer = array[b]               # a[2]
    return answer