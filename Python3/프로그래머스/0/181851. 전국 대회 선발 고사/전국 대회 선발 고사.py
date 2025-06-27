def solution(rank, attendance):
    rankDict = dict(list(zip(rank, attendance)))
    tmp = []
    count = 0
    
    for key, val in rankDict.items():
        if val: tmp.append([count, key])
        count += 1
    
    tmp.sort(key=lambda x : x[1])
    a, b, c = tmp[:3]
    
    return 10000 * a[0] + 100 * b[0] + c[0]