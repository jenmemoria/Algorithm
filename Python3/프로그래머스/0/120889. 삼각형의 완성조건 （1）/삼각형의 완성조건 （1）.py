def solution(sides):
    tri_check = sum(sides) - max(sides)
    if max(sides) < tri_check:
        return 1
    else:
        return 2