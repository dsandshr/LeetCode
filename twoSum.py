class Solution:
    def twoSum(self, nums, target):
        res = dict()
        
        for i in range(len(nums)):
            seeking = target - nums[i]
            if seeking in res:
                return [i, res.get(seeking)]
            res[nums[i]] = i