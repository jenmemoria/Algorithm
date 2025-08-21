def solution(numlist, n):
    answer = []
    bucket = [1] * len(numlist)

    while sum(bucket) > 0:
        absV, absI = 999999, 0
        for i in range(len(numlist)):
            if bucket[i] == 1:
                if abs(n - numlist[i]) < absV:
                    absV = abs(n - numlist[i])
                    absI = i
                elif abs(n - numlist[i]) == absV:
                    if numlist[absI] < numlist[i]:
                        absV = abs(n - numlist[i])
                        absI = i
        bucket[absI] = 0
        answer.append(numlist[absI])

    return answer