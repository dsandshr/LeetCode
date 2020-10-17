class Solution:
    def twoSum(self, nums, target):
        res = dict()
        
        for i, num in enumerate(nums):
            seeking = target - num
            if seeking in res:
                return [res[seeking], i]
            res[num] = i