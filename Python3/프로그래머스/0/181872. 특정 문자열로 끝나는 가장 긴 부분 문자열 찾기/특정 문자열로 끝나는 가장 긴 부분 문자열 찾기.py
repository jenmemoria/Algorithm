def solution(myString, pat):
    if len(pat) > 1:
        num = myString.rindex(pat) + len(pat)
        return myString[:num]
    else:
        num = myString.rindex(pat) + 1
        return myString[:num]