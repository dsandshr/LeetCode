class Solution:
    def twoSum(self, nums, target):
        start_index = 0
        index_end = 1
        lenght = len(nums)
        
        while start_index < lenght:
            if target - nums[start_index] in nums[start_index + 1:]:
                index_end = start_index + 1
                while nums[index_end] != target - nums[start_index]:
                    index_end += 1
                return [start_index, index_end]
            else: start_index += 1