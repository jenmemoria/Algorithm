def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        # 배열의 모든 원소의 합 비교
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0