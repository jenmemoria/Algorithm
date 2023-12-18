def solution(array, height):
    answer = [i for i in array if i > height]
    print(len(answer))
    return len(answer)