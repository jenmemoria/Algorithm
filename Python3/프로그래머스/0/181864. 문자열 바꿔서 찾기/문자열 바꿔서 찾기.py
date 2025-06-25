def solution(myString, pat):
    result = myString.replace("A", "X").replace("B", "A").replace("X", "B")
    return int(pat in result)