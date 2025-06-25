def solution(arr, k):
    answer = []
    
    for a in arr:
        if a not in answer:
            answer.append(a)
            if len(answer) == k:
                break
    
    while len(answer) < k:
        answer.append(-1)
    
    return answer