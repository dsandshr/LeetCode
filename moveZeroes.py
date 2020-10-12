class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1

Solution.moveZeroes(None, [0,2,0,1,3,1,0,0,2,0,8,8,9,0,5])