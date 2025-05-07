def solution(food):
    answer = []

    for i in range(1, len(food)):
        count = food[i] // 2

        if count == 0:
            continue

        answer.append(str(i) * count)

    answer.extend(['0'])
    answer.extend(answer[::-1][1:])

    return "".join(answer)