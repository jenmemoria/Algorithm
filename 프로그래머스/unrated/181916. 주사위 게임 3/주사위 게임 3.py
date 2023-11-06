def solution(a, b, c, d):
    nums = [a, b, c, d]
    sames = [nums.count(i) for i in nums]
    if max(sames) == 4:
        return 1111 * a
    elif max(sames) == 3 :
        p = nums[sames.index(3)]
        q = nums[sames.index(1)]
        return (10 * p + q)**2
    elif max(sames) == 2:
        if (min(sames)) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a-b)
        else:
            p = nums[sames.index(2)]
            return (a*b*c*d)/p**2
    else:
        return min(nums)    