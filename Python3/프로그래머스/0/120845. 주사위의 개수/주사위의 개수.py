def solution(box, n):
    # result는 큐브의 총 개수를 저장할 변수, 처음엔 1로 시작
    result = 1
    
    # box 리스트의 각 차원을 순회하며
    for curr in box:
        # 각 차원의 크기를 큐브의 한 변 길이 n으로 나눈 몫을 계산하여 result에 곱함
        result *= curr // n
    
    # 계산된 총 큐브 개수를 반환
    return result