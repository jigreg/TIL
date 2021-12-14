def arrayPalrSum(self,nums):
    sum = 0
    palr = []
    nums.sort()

    for n in nums :
        palr.append(n)
        if len(palr) == 2:
            sum += min(palr)
            palr = []
    return sum
