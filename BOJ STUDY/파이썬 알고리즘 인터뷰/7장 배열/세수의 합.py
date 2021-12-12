# 브루트 포스
nums = [[-1,0,1],[-1,-1,2]]
def threeSum(self,nums):
    results = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,len(nums)-1):
            if j > i + 1 and nums[j] == nums[j-1]:
                for k in range(j+1,len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i],nums[j],nums[k]])
    return results

    